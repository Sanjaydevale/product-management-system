
A robust and simple Product Management API built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features

-   **RESTful API**: Manage products (Create, Read, Update, Delete).
-   **Database**: PostgreSQL integration using SQLAlchemy ORM.
-   **Validation**: Data validation using Pydantic models.
-   **CORS Support**: Configured for frontend integration (React, etc.).

## Prerequisites

-   Python 3.8+
-   PostgreSQL installed and running.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Create a `.env` file in the root directory.
2.  Add your database credentials:
    ```env
    DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
    ```
    *Example:* `DATABASE_URL=postgresql://postgres:pass123@localhost:5432/database_1`

## Running the Application

Start the development server with `uvicorn`:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

FastAPI provides automatic interactive documentation. Once the server is running, visit:

-   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs) - Test endpoints directly in your browser.
-   **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc) - Alternative documentation view.

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check / Greeting. |
| `GET` | `/products` | List all available products. |
| `GET` | `/products/{id}` | Get details of a specific product. |
| `POST` | `/products` | Add a new product. |
| `PUT` | `/products/{id}` | Update an existing product. |
| `DELETE` | `/products/{id}` | Delete a product. |

## Project Structure

```
├── frontend/          # React Application
├── database.py        # Database connection and session setup
├── database_models.py # SQLAlchemy database models
├── main.py            # Application entry point and API routes
├── models.py          # Pydantic data schemas
├── requirements.txt   # Python dependencies
└── .env               # Environment variables (not committed)
```
