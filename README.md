# Todo API

A RESTful API built with FastAPI and SQLite, demonstrating backend development fundamentals in Python.

## Tech Stack
- **Framework**: FastAPI (Python)
- **Database**: SQLite via SQLAlchemy ORM
- **Validation**: Pydantic
- **Server**: Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /todos | Get all todos |
| POST | /todos | Create a new todo |
| GET | /todos/{id} | Get a todo by ID |
| PUT | /todos/{id} | Update a todo |
| DELETE | /todos/{id} | Delete a todo |

## Run Locally

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

## Author
Haochen Li | SMU Computer Engineering | github.com/Haochen0416
