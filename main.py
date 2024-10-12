from fastapi import FastAPI
import models
from database import engine
from app.auth.auth_routes import router as auth_router
from app.todo.todo_routes import router as todo_router

app = FastAPI(
    servers=[
        {"url": "http://localhost:8000", "description": "Local server"}
    ]
)
models.Base.metadata.create_all(bind=engine)

app.include_router(router=auth_router, prefix="/auth")
app.include_router(router=todo_router, prefix="/todo")
