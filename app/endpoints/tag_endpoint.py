from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.core.database import get_db
from ..crud import tag_crud
from app.schemas.tag import TagSchema

router = APIRouter(prefix='/tag')


@router.get('/', response_model=List[TagSchema])
async def get_all_tags(db: Session = Depends(get_db)):
    tags = tag_crud.get_all_tags(db=db, limit=100)
    return tags


@router.get('/{id}', response_model=TagSchema)
async def get_tag_by_id(id: int, db: Session = Depends(get_db)):
    tag = tag_crud.get_tag_by_id(db=db, tag_id=id)
    return tag


@router.post('/', response_model=TagSchema)
async def create_tag(tag: TagSchema, db: Session = Depends(get_db)):
    _tag = tag_crud.create_tag(db=db, tag=tag)
    return _tag


@router.put('/{id}', response_model=TagSchema)
async def update_tag(id: int, tag: TagSchema, db: Session = Depends(get_db)):
    _tag = tag_crud.update_tag(db=db, tag_id=id, name=tag.name)
    return _tag


@router.delete('/{id}', response_model=int)
async def remove_tag(id: int, db: Session = Depends(get_db)):
    tag_crud.remove_tag(db=db, tag_id=id)
    return id
