from sqlalchemy.orm import Session

from app.core.models import Photo
from app.schemas.photo import PhotoSchema


def get_all_photos(db: Session, limit: int = 100):
    return db.query(Photo).limit(limit).all()


def get_photo_by_id(db: Session, photo_id: int):
    return db.query(Photo).filter(Photo.id == photo_id).first()


def create_photo(db: Session, photo: PhotoSchema):
    _photo = Photo(dish_id=photo.dish_id, link=photo.link)
    db.add(_photo)
    db.commit()
    db.refresh(_photo)
    return _photo


def remove_photo(db: Session, photo_id: int):
    _photo = get_photo_by_id(db=db, photo_id=photo_id)
    db.delete(_photo)
    db.commit()


def update_photo(db: Session, photo_id: int, dish_id: int, link: str):
    _photo = get_photo_by_id(db=db, photo_id=photo_id)
    _photo.dish_id = dish_id
    _photo.link = link
    db.commit()
    db.refresh(_photo)
    return _photo


def get_all_photos_by_dish_id(db: Session, dish_id: int):
    return db.query(Photo).filter(Photo.dish_id == dish_id).all()
