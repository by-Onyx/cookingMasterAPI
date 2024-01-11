from typing import List, Tuple

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..core.models import Tag
from ..crud import dish_crud, photo_crud, dish_tag_crud, tag_crud, dish_category_crud, category_crud
from ..schemas.category import CategorySchema
from ..schemas.dish import DishSchema, DishFullSchema, DishTagSchema, DishCategorySchema
from ..schemas.photo import PhotoSchema, PhotoSchemaForDish
from ..schemas.tag import TagSchema

router = APIRouter(prefix='/dish')


@router.get('/', response_model=List[DishSchema])
async def get_all_dishes(db: Session = Depends(get_db)):
    dishes = dish_crud.get_all_dishes(db=db, limit=100)
    return dishes


@router.get('/{id}', response_model=DishSchema)
async def get_dish_by_id(id: int, db: Session = Depends(get_db)):
    dishes = dish_crud.get_dish_by_id(db=db, dish_id=id)
    return dishes


@router.post('/', response_model=DishSchema)
async def create_dish(request: DishSchema, db: Session = Depends(get_db)):
    _dish = dish_crud.create_dish(db=db, dish=request)
    return _dish


@router.put('/{id}', response_model=DishSchema)
async def update_dish(id: int, request: DishSchema, db: Session = Depends(get_db)):
    _dish = dish_crud.update_dish(db=db,
                                  dish_id=id,
                                  name=request.name,
                                  cookingTime=request.cookingTime,
                                  receipt=request.receipt,
                                  products=request.products)
    return _dish


@router.delete('/{id}', response_model=int)
async def remove_dish(id: int, db: Session = Depends(get_db)):
    _dish = dish_crud.remove_dish(db=db, dish_id=id)
    return id


@router.get('/{id}/full_info', response_model=DishFullSchema)
async def get_dish_full_info(id: int, db: Session = Depends(get_db)):
    _dish = dish_crud.get_dish_by_id(db=db, dish_id=id)
    _photos = photo_crud.get_all_photos_by_dish_id(db=db, dish_id=id)

    _tag_ids = dish_tag_crud.get_all_tags_by_dish_id(db=db, dish_id=id)
    _tags = [tag_crud.get_tag_by_id(db=db, tag_id=tag_id[0])
             for tag_id in _tag_ids]

    _category_ids = dish_category_crud.get_all_categories_by_dish_id(db=db, dish_id=id)
    _categories = [category_crud.get_category_by_id(db=db, category_id=category_id[0])
                   for category_id in _category_ids]

    return DishFullSchema(
        id=_dish.id,
        name=_dish.name,
        cookingTime=_dish.cookingTime,
        receipt=_dish.receipt,
        products=_dish.products,
        photos=[PhotoSchemaForDish(id=photo.id, link=photo.link)
                for photo in _photos],
        tags=[TagSchema(id=tag.id, name=tag.name)
              for tag in _tags],
        categories=[CategorySchema(id=category.id, name=category.name)
                    for category in _categories]
    )


@router.post('/{id}/add_tag/{tag_id}', response_model=DishTagSchema)
async def add_tag_to_dish(id: int, tag_id: int, db: Session = Depends(get_db)):
    _dish_tag = dish_tag_crud.add_tag_to_dish(db=db, dish_id=id, tag_id=tag_id)
    return DishTagSchema(
        dish_id=_dish_tag.dish_id,
        tag_id=_dish_tag.tag_id
    )


@router.post('/{id}/add_category/{category_id}', response_model=DishCategorySchema)
async def add_tag_to_dish(id: int, category_id: int, db: Session = Depends(get_db)):
    _dish_category = (dish_category_crud
                      .add_category_to_dish(db=db, dish_id=id, category_id=category_id))
    return DishCategorySchema(
        dish_id=_dish_category.dish_id,
        category_id=_dish_category.category_id
    )


@router.delete('/{id}/delete_tag/{tag_id}', response_model=DishCategorySchema)
async def delete_tag_from_dish(id: int, tag_id: int, db: Session = Depends(get_db)):
    dish_tag_crud.delete_tag_from_dish(db=db, dish_id=id, tag_id=tag_id)
    return DishTagSchema(
        dish_id=id,
        tag_id=tag_id
    )


@router.delete('/{id}/delete_category/{category_id}', response_model=DishCategorySchema)
async def add_tag_to_dish(id: int, category_id: int, db: Session = Depends(get_db)):
    dish_category_crud.delete_category_from_dish(db=db, dish_id=id, category_id=category_id)
    return DishCategorySchema(
        dish_id=id,
        category_id=category_id
    )