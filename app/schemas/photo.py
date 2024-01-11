from typing import Optional

from pydantic import BaseModel


class PhotoSchema(BaseModel):
    id: Optional[int] = None
    dish_id: Optional[int] = None
    link: Optional[str] = None

    class Config:
        orm_mode = True


class PhotoSchemaForDish(BaseModel):
    id: Optional[int] = None
    link: Optional[str] = None
