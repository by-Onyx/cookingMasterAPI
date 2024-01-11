from typing import Optional

from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True
    