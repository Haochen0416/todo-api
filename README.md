# Todo API with JWT Authentication

A production-ready RESTful API built with FastAPI, SQLite, and JWT authentication, demonstrating core backend development skills in Python.

## Features

- **JWT Authentication** – Secure user registration, login, and token-based access control
- **RESTful API** – Full CRUD operations following REST principles
- **Database ORM** – SQLAlchemy with SQLite for data persistence
- **Data Validation** – Pydantic schemas for request/response validation
- **Auto Documentation** – Interactive Swagger UI at `/docs`
- **Protected Endpoints** – Todo operations require valid JWT token

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI (Python) |
| Database | SQLite via SQLAlchemy ORM |
| Authentication | JWT (python-jose) + bcrypt password hashing |
| Validation | Pydantic v2 |
| Server | Uvicorn |

## API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /auth/register | Register a new user | No |
| POST | /auth/login | Login and get JWT token | No |
| GET | /auth/me | Get current user info | Yes |

### Todos
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /todos | Get all todos for current user | Yes |
| POST | /todos | Create a new todo | Yes |
| PUT | /todos/{id} | Update a todo | Yes |
| DELETE | /todos/{id} | Delete a todo | Yes |

## Run Locally

```bash
# Install dependencies
pip install fastapi uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt] python-multipart

# Start the server
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

## Project Structure

    todo-api/
    ├── main.py          # FastAPI app, routes, and Pydantic schemas
    ├── models.py        # SQLAlchemy database models (User, Todo)
    ├── database.py      # Database connection and session management
    ├── auth.py          # JWT token creation and verification
    └── requirements.txt # Project dependencies

## Author
Haochen Li | SMU Computer Engineering | [github.com/Haochen0416](https://github.com/Haochen0416)