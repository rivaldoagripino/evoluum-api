from fastapi import APIRouter, HTTPException

from app.auth.auth_schemas import AuthResponse
from settings import Settings


router = APIRouter(tags=["Auth"])


@router.get("/token", response_model=AuthResponse)
async def get_token():
    token = Settings.STATIC_TOKEN
    if not token:
        raise HTTPException(status_code=404)
    return AuthResponse(token=token)
