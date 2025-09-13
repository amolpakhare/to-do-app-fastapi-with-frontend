from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette import status

from .schem import TodoCreate, TodoUpdate

from .service import (
    createation_todo,
    update_todo,
    delete_todo,
    get_todo,
    get_todos
)
from database import get_db

router = APIRouter(tags=["TODOAPI"])
templates = Jinja2Templates(directory="template")

# ---------------- API ROUTES ---------------- #

@router.post("/Creation")
def todo_creation(todo: TodoCreate, db: Session = Depends(get_db)):
    return createation_todo(db, todo)

@router.put("/update/{todo_id}")
def todo_updation(todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_db)):
    return update_todo(db, todo_id, todo_in)

@router.delete("/delete/{todo_id}")
def todo_deletion(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo(db, todo_id)

@router.get("/todo/{todo_id}")
def show_todo_byid(todo_id: int, db: Session = Depends(get_db)):
    return get_todo(db, todo_id)

@router.get("/todos")
def show_todos(db: Session = Depends(get_db)):
    return get_todos(db)

# ---------------- HTML ROUTES ---------------- #

# Home Page - Show all todos
@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    todos = get_todos(db)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

# Create Page - GET + POST
@router.get("/create")
def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@router.post("/create")
def create_task(title: str = Form(...), description: str = Form(""), db: Session = Depends(get_db)):
    todo = TodoCreate(title=title, description=description)
    createation_todo(db, todo)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

# Edit Page - GET + POST
@router.get("/edit/{todo_id}")
def edit_page(todo_id: int, request: Request, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return templates.TemplateResponse("edit.html", {"request": request, "todo": todo})

@router.post("/edit/{todo_id}")
def edit_task(todo_id: int, title: str = Form(...), description: str = Form(""), completed: bool = Form(False), db: Session = Depends(get_db)):
    todo_update = TodoUpdate(title=title, description=description, completed=completed)
    update_todo(db, todo_id, todo_update)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

# Delete task (from HTML form)
@router.post("/delete/{todo_id}")
def delete_task(todo_id: int, db: Session = Depends(get_db)):
    delete_todo(db, todo_id)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


















#from fastapi import APIRouter,Depends,HTTPException
# from sqlalchemy.orm import session
# from schem import (TodoCreate,TodoUpdate,TodoInDBBase)
# from service import (createation_todo,update_todo,delete_todo,get_todo,get_todos)
# from ..database import get_db

# router = APIRouter(tags=["TODOAPI"])

# @router.post("/Creation")
# def todo_creation(todo:TodoCreate,db:session=Depends(get_db)):
#     return createation_todo(db,todo)

# @router.put("/")
# def todo_updation(todo_id:int,todo_in:TodoUpdate,db:session=Depends(get_db)):
#     return update_todo(db,todo_id,todo_in)

# @router.delete("/")
# def todo_deletion(todo_id:int,db:session=Depends(get_db)):
#     return delete_todo(db,todo_id)

# @router.get("/")
# def show_todo_byid(todo_id:int,db:session=Depends(get_db)):
#     return get_todo(db,todo_id)

# @router.get("/")
# def show_todos(db:session=Depends(get_db)):
#     return get_todos(db)