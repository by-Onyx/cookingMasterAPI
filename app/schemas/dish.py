from typing import Optional, List

from pydantic import BaseModel

from app.schemas.category import CategorySchema
from app.schemas.photo import PhotoSchemaForDish
from app.schemas.tag import TagSchema


class DishSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    cookingTime: Optional[int] = None
    receipt: Optional[str] = None
    products: Optional[str] = None

    class Config:
        orm_mode = True


class DishFullSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    cookingTime: Optional[int] = None
    receipt: Optional[str] = None
    products: Optional[str] = None
    photos: Optional[List[PhotoSchemaForDish]] = None
    tags: Optional[List[TagSchema]] = None
    categories: Optional[List[CategorySchema]] = None


class DishTagSchema(BaseModel):
    dish_id: Optional[int] = None
    tag_id: Optional[int] = None


class DishCategorySchema(BaseModel):
    dish_id: Optional[int] = None
    category_id: Optional[int] = None
