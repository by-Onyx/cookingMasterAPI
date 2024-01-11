from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from ..crud import category_crud
from app.schemas.category import CategorySchema

router = APIRouter(prefix='/category')


@router.get('/', response_model=List[CategorySchema])
async def get_all_categories(db: Session = Depends(get_db)):
    categories = category_crud.get_all_categories(db=db, limit=100)
    return categories


@router.get('/{id}', response_model=CategorySchema)
async def get_category_by_id(id: int, db: Session = Depends(get_db)):
    category = category_crud.get_category_by_id(db=db, category_id=id)
    return category


@router.post('/', response_model=CategorySchema)
async def create_category(category: CategorySchema, db: Session = Depends(get_db)):
    _category = category_crud.create_category(db=db, category=category)
    return _category


@router.put('/{id}', response_model=CategorySchema)
async def update_category(id: int, category: CategorySchema, db: Session = Depends(get_db)):
    _category = category_crud.update_category(db=db, category_id=id, name=category.name)
    return _category


@router.delete('/{id}', response_model=int)
async def remove_category(id: int, db: Session = Depends(get_db)):
    category_crud.remove_category(db=db, category_id=id)
    return id
