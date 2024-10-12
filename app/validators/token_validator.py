from fastapi import HTTPException, Header
from settings import Settings


async def token_validator(token: str = Header(...)):
    if token != Settings.STATIC_TOKEN:
        raise HTTPException(status_code=403, detail="Permissão negada")
