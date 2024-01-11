from typing import List

from sqlalchemy.orm import Session

from app.core.models import DishTag


def get_all_tags_by_dish_id(db: Session, dish_id: int):
    return db.query(DishTag.tag_id).filter(DishTag.dish_id == dish_id).all()


def add_tag_to_dish(db: Session, dish_id: int, tag_id: int):
    _dish_tag = DishTag(tag_id=tag_id, dish_id=dish_id)
    db.add(_dish_tag)
    db.commit()
    db.refresh(_dish_tag)
    return _dish_tag


def delete_tag_from_dish(db: Session, dish_id: int, tag_id: int):
    _dish_tag = (db
                 .query(DishTag)
                 .filter(DishTag.dish_id == dish_id)
                 .filter(DishTag.tag_id == tag_id)
                 .first())
    db.delete(_dish_tag)
    db.commit()
