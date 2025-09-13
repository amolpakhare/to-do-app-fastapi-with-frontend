# FastAPI TODO App

A **backend-focused TODO application** built using **FastAPI** and **SQLAlchemy**. This project demonstrates robust API development, secure user authentication, and database management with Python.
 Built during my Python training at EPPS Infotech pvt ltd pune as part of learning practical backend development.


## **Project Overview**

This TODO app allows users to:

- Register and login securely
- Create, read, update, and delete TODO tasks
- Authenticate with JWT tokens
- Interact with the backend via **RESTful API endpoints**
- Explore the API with Swagger UI

The frontend is minimal (HTML, CSS, JavaScript) and primarily serves to test API interactions.

---

## **Backend Skills / Tech Stack**

- **Python** – Core backend programming
- **FastAPI** – High-performance web framework and API development
- **SQLAlchemy** – ORM for handling database models and queries
- **JWT Authentication** – Secure token-based authentication
- **SQLite** – Lightweight relational database

**Other Skills:** HTML, CSS, JavaScript (for minimal frontend interaction)

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/amolpakhare/fastapi-todo-app.git
cd fastapi-todo-app

## **Endpoits**

| Endpoint     | Method | Description             |
| ------------ | ------ | ----------------------- |
| `/register`  | POST   | Register a new user     |
| `/login`     | POST   | Login and get JWT token |
| `/todo/`     | POST   | Create a new TODO task  |
| `/todo/`     | GET    | Get all TODO tasks      |
| `/todo/{id}` | PUT    | Update a TODO task      |
| `/todo/{id}` | DELETE | Delete a TODO task      |


## **fastapi-todo-app/**
│
├── main.py           # Entry point / FastAPI app
├── database.py       # Database setup with SQLAlchemy
├── requirements.txt
├── todo.db           # SQLite database
├── templates/        # Optional minimal HTML templates
├── static/           # Optional CSS/JS files
└── todo/             # Backend modules for routes and services

Note: 
