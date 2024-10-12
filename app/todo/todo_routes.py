
from typing import List
from fastapi import APIRouter, Depends, HTTPException

from app.todo.todo_controller import TodoController
from app.todo.todo_schemas import TodoCreate, TodoResponse
from sqlalchemy.orm import Session

from database import get_db



router = APIRouter(
    tags=["Todo"]
)
todo_controller = TodoController()

@router.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_controller.create_todo(todo, db)

@router.get("/todos", response_model=List[TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return todo_controller.get_all_todos(db)

@router.get("/todos/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_controller.get_todo_by_id(todo_id, db)
    if not todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return todo

@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, updated_todo: TodoCreate, db: Session = Depends(get_db)):
    todo = todo_controller.update_todo(todo_id, updated_todo, db)
    if not todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return todo

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    success = todo_controller.delete_todo(todo_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return {"message": "Tarefa deletada com sucesso!"}