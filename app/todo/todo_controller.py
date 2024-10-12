from typing import List, Optional
from sqlalchemy.orm import Session

from app.todo.todo_schemas import TodoCreate
from models import TodoItem

class TodoController:
    def create_todo(self, todo: TodoCreate, db: Session) -> TodoItem:
        new_todo = TodoItem(**todo.dict())
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return new_todo

    def get_all_todos(self, db: Session) -> List[TodoItem]:
        return db.query(TodoItem).all()

    def get_todo_by_id(self, todo_id: int, db: Session) -> Optional[TodoItem]:
        return db.query(TodoItem).filter(TodoItem.id == todo_id).first()

    def update_todo(self, todo_id: int, updated_todo: TodoCreate, db: Session) -> Optional[TodoItem]:
        todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
        if todo:
            for key, value in updated_todo.dict().items():
                setattr(todo, key, value)
            db.commit()
            return todo
        return None

    def delete_todo(self, todo_id: int, db: Session) -> bool:
        todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
        if todo:
            db.delete(todo)
            db.commit()
            return True
        return False