from sqlalchemy.orm import Session

from app.core.models import DishCategory


def get_all_categories_by_dish_id(db: Session, dish_id: int):
    return db.query(DishCategory.category_id).filter(DishCategory.dish_id == dish_id).all()


def add_category_to_dish(db: Session, dish_id: int, category_id: int):
    _dish_category = DishCategory(dish_id=dish_id, category_id=category_id)
    db.add(_dish_category)
    db.commit()
    db.refresh(_dish_category)
    return _dish_category


def delete_category_from_dish(db: Session, dish_id: int, category_id: int):
    _dish_category = (db
                      .query(DishCategory)
                      .filter(DishCategory.dish_id == dish_id)
                      .filter(DishCategory.category_id == category_id)
                      .first())
    db.delete(_dish_category)
    db.commit()
