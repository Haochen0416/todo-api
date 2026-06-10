# 🔐 Todo API — Production-Ready REST API with JWT Authentication

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite&logoColor=white)](https://sqlite.org)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=flat&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

A **production-ready RESTful API** built with FastAPI, SQLAlchemy, and JWT authentication — demonstrating secure backend development patterns in Python including user auth, ORM-based persistence, and auto-generated API documentation.

---

## ✨ Features

- 🔐 **JWT Authentication** — Secure user registration, login, and token-based access control
- 🗄️ **SQLAlchemy ORM** — Clean database layer with SQLite, easily swappable to PostgreSQL
- ✅ **Pydantic Validation** — Request/response validation with detailed error messages
- 📖 **Auto Documentation** — Interactive Swagger UI at `/docs`, ReDoc at `/redoc`
- 🔒 **Protected Endpoints** — All todo operations require a valid JWT bearer token
- 🏗️ **Modular Architecture** — Separated concerns: routes, models, database, auth

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI (Python) |
| Database | SQLite via SQLAlchemy ORM |
| Authentication | JWT (`python-jose`) + bcrypt password hashing |
| Validation | Pydantic v2 |
| Server | Uvicorn (ASGI) |

---

## 📡 API Endpoints

### 🔑 Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:-------------:|
| `POST` | `/auth/register` | Register a new user | ❌ |
| `POST` | `/auth/login` | Login and receive JWT token | ❌ |
| `GET` | `/auth/me` | Get current authenticated user | ✅ |

### ✅ Todos

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:-------------:|
| `GET` | `/todos` | List all todos for current user | ✅ |
| `POST` | `/todos` | Create a new todo | ✅ |
| `PUT` | `/todos/{id}` | Update an existing todo | ✅ |
| `DELETE` | `/todos/{id}` | Delete a todo | ✅ |

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Haochen0416/todo-api.git
cd todo-api

# Install dependencies
pip install -r requirements.txt

# Start the development server
uvicorn main:app --reload
```

Visit **http://127.0.0.1:8000/docs** for the interactive Swagger UI.

---

## 📁 Project Structure

```
todo-api/
├── main.py          # FastAPI app, route handlers, and Pydantic schemas
├── models.py        # SQLAlchemy database models (User, Todo)
├── database.py      # DB engine, session factory, and Base declaration
├── auth.py          # JWT token creation, verification, and password hashing
├── requirements.txt # Pinned project dependencies
└── .gitignore
```

---

## 🔄 Auth Flow

```
1. POST /auth/register  →  Hash password with bcrypt, store user in DB
2. POST /auth/login     →  Verify credentials, return signed JWT token
3. GET  /todos          →  Decode JWT from Authorization header, return user's todos
```

---

## 💡 Key Implementation Details

- **Password Security**: bcrypt hashing via `passlib` — plaintext passwords never stored
- **Token Design**: HS256-signed JWT with configurable expiry and user ID as subject
- **ORM Patterns**: SQLAlchemy declarative models with relationship between `User` and `Todo`
- **Dependency Injection**: FastAPI `Depends()` for clean auth middleware on protected routes
- **Schema Separation**: Pydantic request/response schemas decoupled from SQLAlchemy models

---

## 🧪 Example Usage

```bash
# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "haochen", "password": "secret123"}'

# Login → get token
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "haochen", "password": "secret123"}'

# Create todo with token
curl -X POST http://localhost:8000/todos \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "completed": false}'
```

---

## 👤 Author

**Haochen Li**  
M.S. Computer Engineering — Southern Methodist University (SMU), Dallas TX  
📧 haochenl@smu.edu · 🔗 [github.com/Haochen0416](https://github.com/Haochen0416)
