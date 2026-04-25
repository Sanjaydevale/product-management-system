from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker


import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
if not db_url:
    db_url = "sqlite:///./product_manager.db"

engine=create_engine(db_url, connect_args={"check_same_thread": False} if db_url.startswith("sqlite") else {})
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
