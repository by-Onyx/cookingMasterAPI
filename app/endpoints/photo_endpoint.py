from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from ..crud import photo_crud
from app.schemas.photo import PhotoSchema

router = APIRouter(prefix='/photo')


@router.get('/', response_model=List[PhotoSchema])
async def get_all_photos(db: Session = Depends(get_db)):
    photos = photo_crud.get_all_photos(db=db, limit=100)
    return photos


@router.get('/{id}', response_model=PhotoSchema)
async def get_photo_by_id(id: int, db: Session = Depends(get_db)):
    photo = photo_crud.get_photo_by_id(db=db, photo_id=id)
    return photo


@router.post('/', response_model=PhotoSchema)
async def create_photo(photo: PhotoSchema, db: Session = Depends(get_db)):
    _photo = photo_crud.create_photo(db=db, photo=photo)
    return _photo


@router.put('/{id}', response_model=PhotoSchema)
async def update_photo(id: int, photo: PhotoSchema, db: Session = Depends(get_db)):
    _photo = photo_crud.update_photo(db=db, photo_id=id, dish_id=photo.dish_id, link=photo.link)
    return _photo


@router.delete('/{id}', response_model=int)
async def remove_photo(id: int, db: Session = Depends(get_db)):
    photo_crud.remove_photo(db=db, photo_id=id)
    return id
