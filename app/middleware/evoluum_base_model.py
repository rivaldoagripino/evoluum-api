from fastapi import HTTPException
from pydantic import BaseModel, Extra, ValidationError

class EvoluumBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid

    def is_valid(self, raise_exception: bool = False) -> bool:
        try:
            self.model_validate()
            return True
        except ValidationError as e:
            if raise_exception:
                raise HTTPException(status_code=400, detail=e.errors())
            return False