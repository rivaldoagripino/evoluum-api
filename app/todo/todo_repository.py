from typing import List, Optional
from sqlalchemy.orm import Session
from app.todo.todo_schemas import TodoCreate
from models import TodoItem


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, todo: TodoCreate) -> TodoItem:
        new_todo = TodoItem(**todo.dict())
        self.db.add(new_todo)
        self.db.commit()
        self.db.refresh(new_todo)
        return new_todo

    def get_all(self) -> List[TodoItem]:
        return self.db.query(TodoItem).all()

    def get_by_id(self, todo_id: int) -> Optional[TodoItem]:
        return self.db.query(TodoItem).filter(TodoItem.id == todo_id).first()

    def update(self,
               todo_id: int,
               updated_todo: TodoCreate) -> Optional[TodoItem]:
        todo = self.db.query(TodoItem).filter(TodoItem.id == todo_id).first()
        if todo:
            for key, value in updated_todo.dict().items():
                setattr(todo, key, value)
            self.db.commit()
            return todo
        return None

    def delete(self, todo_id: int) -> bool:
        todo = self.db.query(TodoItem).filter(TodoItem.id == todo_id).first()
        if todo:
            self.db.delete(todo)
            self.db.commit()
            return True
        return False
