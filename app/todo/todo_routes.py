from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.todo.todo_controller import TodoController
from app.todo.todo_schemas import TodoCreate, TodoResponse
from app.validators.token_validator import token_validator
from database import get_db

router = APIRouter(tags=["Todo"])


@router.post("/todos", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    token: str = Depends(token_validator),
):
    controller = TodoController(db)
    return controller.create_todo(todo)


@router.get("/todos", response_model=List[TodoResponse])
def read_todos(db: Session = Depends(get_db), token: str = Depends(token_validator)):
    controller = TodoController(db)
    todo_list = controller.get_all_todos()
    if not todo_list:
        raise HTTPException(status_code=204, detail=[])
    return todo_list


@router.get("/todos/{todo_id}", response_model=TodoResponse)
def read_todo(
    todo_id: int, db: Session = Depends(get_db), token: str = Depends(token_validator)
):
    controller = TodoController(db)
    todo = controller.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return todo


@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    updated_todo: TodoCreate,
    db: Session = Depends(get_db),
    token: str = Depends(token_validator),
):
    controller = TodoController(db)
    todo = controller.update_todo(todo_id, updated_todo)
    if not todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return todo


@router.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int, db: Session = Depends(get_db), token: str = Depends(token_validator)
):
    controller = TodoController(db)
    success = controller.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return {"message": "Tarefa deletada com sucesso!"}
