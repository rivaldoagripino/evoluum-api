from typing import List, Optional
from sqlalchemy.orm import Session

from app.todo.todo_schemas import TodoCreate, TodoResponse
from app.todo.todo_repository import TodoRepository
from models import TodoItem

class TodoController:
    def __init__(self, db: Session):
        self.repository = TodoRepository(db)

    def create_todo(self, todo: TodoCreate) -> TodoItem:
        created_todo = self.repository.create(todo)
        return TodoResponse(
            id=created_todo.id,
            title=created_todo.title,
            description=created_todo.description,
            created_at=created_todo.created_at.isoformat(),
            updated_at=created_todo.updated_at.isoformat(),
        )

    def get_all_todos(self) -> List[TodoItem]:
        todo_list = self.repository.get_all()
        return [TodoResponse(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            created_at=todo.created_at.isoformat(),
            updated_at=todo.updated_at.isoformat(),
        ) for todo in todo_list]

    def get_todo_by_id(self, todo_id: int) -> Optional[TodoItem]:
        return self.repository.get_by_id(todo_id)

    def update_todo(self, todo_id: int, updated_todo: TodoCreate) -> Optional[TodoItem]:
        return self.repository.update(todo_id, updated_todo)

    def delete_todo(self, todo_id: int) -> bool:
        return self.repository.delete(todo_id)
