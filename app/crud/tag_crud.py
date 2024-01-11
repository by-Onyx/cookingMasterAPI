from sqlalchemy.orm import Session

from app.core.models import Tag
from app.schemas.tag import TagSchema


def get_all_tags(db: Session, limit: int = 100):
    return db.query(Tag).limit(limit).all()


def get_tag_by_id(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()


def create_tag(db: Session, tag: TagSchema):
    _tag = Tag(name=tag.name)
    db.add(_tag)
    db.commit()
    db.refresh(_tag)
    return _tag


def remove_tag(db: Session, tag_id: int):
    _tag = get_tag_by_id(db=db, tag_id=tag_id)
    db.delete(_tag)
    db.commit()


def update_tag(db: Session, tag_id: int, name: str):
    _tag = get_tag_by_id(db=db, tag_id=tag_id)
    _tag.name = name
    db.commit()
    db.refresh(_tag)
    return _tag
