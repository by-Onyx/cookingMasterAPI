from typing import Optional

from pydantic import BaseModel


class TagSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True
