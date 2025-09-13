from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schem



#POST
def createation_todo(db: Session, todo: schem.TodoCreate) -> models.Todo:
    db_todo = models.Todo(title=todo.title, description=todo.description, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

#GET
def get_todo(db: Session, todo_id: int) -> Optional[models.Todo]:
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

#GET
def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    return db.query(models.Todo).offset(skip).limit(limit).all()

#PUt
def update_todo(db: Session, todo_id: int, todo_in: schem.TodoUpdate) -> Optional[models.Todo]:
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None
    if todo_in.title is not None:
        db_todo.title = todo_in.title
    if todo_in.description is not None:
        db_todo.description = todo_in.description
    if todo_in.completed is not None:
        db_todo.completed = todo_in.completed
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


#DELETE
def delete_todo(db: Session, todo_id: int) -> bool:
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True
