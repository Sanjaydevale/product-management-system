from fastapi import FastAPI,Depends,HTTPException
from contextlib import asynccontextmanager
from models import Product, ProductBase
from database import session,engine
import database_models
from sqlalchemy.orm import Session

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app=FastAPI(lifespan=lifespan)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello, World!"

products=[
    
    Product(id=1,name="phone",description="smartphone",price=699.99,quantity=50),
    Product(id=2,name="laptop",description="gaming laptop",price=1299.99,quantity=30),
    Product(id=3,name="headphones",description="wireless headphones",price=199.99,quantity=100)
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
    

def init_db():
    db=session()
    count=db.query(database_models.Product).count()
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
    
    
    


@app.get("/products", response_model=list[Product])
def all_products(db:Session=Depends(get_db)):

    db_products=db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}", response_model=Product)
def get_product_by_id(id:int, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", response_model=Product)
def add_product(product:ProductBase, db:Session=Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/products/{id}", response_model=Product)
def update_product(id:int,updated_product:ProductBase, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_product.name = updated_product.name
    db_product.description = updated_product.description
    db_product.price = updated_product.price
    db_product.quantity = updated_product.quantity
    
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{id}")
def delete_product(id:int, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

