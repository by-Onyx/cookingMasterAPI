from sqlalchemy.orm import Session

from app.core.models import Category
from app.schemas.category import CategorySchema


def get_all_categories(db: Session, limit: int = 100):
    return db.query(Category).limit(limit).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(db: Session, category: CategorySchema):
    _category = Category(name=category.name)
    db.add(_category)
    db.commit()
    db.refresh(_category)
    return _category


def remove_category(db: Session, category_id: int):
    _category = get_category_by_id(db=db, category_id=category_id)
    db.delete(_category)
    db.commit()


def update_category(db: Session, category_id: int, name: str):
    _category = get_category_by_id(db=db, category_id=category_id)
    _category.name = name
    db.commit()
    db.refresh(_category)
    return _category
