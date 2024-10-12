from typing import List, Optional
from sqlalchemy.orm import Session

from app.todo.todo_schemas import TodoCreate
from app.todo.todo_repository import TodoRepository
from models import TodoItem

class TodoController:
    def __init__(self, db: Session):
        self.repository = TodoRepository(db)

    def create_todo(self, todo: TodoCreate) -> TodoItem:
        return self.repository.create(todo)

    def get_all_todos(self) -> List[TodoItem]:
        return self.repository.get_all()

    def get_todo_by_id(self, todo_id: int) -> Optional[TodoItem]:
        return self.repository.get_by_id(todo_id)

    def update_todo(self, todo_id: int, updated_todo: TodoCreate) -> Optional[TodoItem]:
        return self.repository.update(todo_id, updated_todo)

    def delete_todo(self, todo_id: int) -> bool:
        return self.repository.delete(todo_id)
