from sqlalchemy.orm import Session
from app.core.models import Dish
from app.schemas.dish import DishSchema


def get_all_dishes(db: Session, limit: int = 100):
    return db.query(Dish).limit(limit).all()


def get_dish_by_id(db: Session, dish_id: int):
    return db.query(Dish).filter(Dish.id == dish_id).first()


def create_dish(db: Session, dish: DishSchema):
    _dish = Dish(name=dish.name,
                 cookingTime=dish.cookingTime,
                 receipt=dish.receipt,
                 products=dish.products)
    db.add(_dish)
    db.commit()
    db.refresh(_dish)
    return _dish


def remove_dish(db: Session, dish_id: int):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    db.delete(_dish)
    db.commit()


def update_dish(db: Session,
                dish_id: int,
                name: str,
                cookingTime: int,
                receipt: str,
                products: str):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    _dish.name = name
    _dish.cookingTime = cookingTime
    _dish.receipt = receipt
    _dish.products = products
    db.commit()
    db.refresh(_dish)
    return _dish


def get_dish_by_name(db: Session, name: str):
    return db.query(Dish.id).filter(Dish.name.icontains(name)).all()
