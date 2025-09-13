from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Base,engine

# Import your router
from todo.router import router as todo_router


Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="Todo App with FastAPI + SQLite")

# Mount static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates (Jinja2)
templates = Jinja2Templates(directory="templates")

# Include routes
app.include_router(todo_router)

# Root redirect (optional)
@app.get("/")
def root():
    return {"message": "Todo App Running! Visit / in browser to see UI."}
