from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from app.core.database import Base, engine


class Dish(Base):
    __tablename__ = 'dish'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100), nullable=False, unique=True)
    cookingTime = Column(Integer, nullable=False)
    receipt = Column(VARCHAR(1024), nullable=False)
    products = Column(VARCHAR(1024), nullable=False)


class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey('dish.id', ondelete='CASCADE'), nullable=False)
    link = Column(VARCHAR(1024), nullable=False)


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100), nullable=False, unique=True)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100), nullable=False, unique=True)


class DishTag(Base):
    __tablename__ = 'dish_tag'

    dish_id = Column(Integer, ForeignKey('dish.id', ondelete='CASCADE'), nullable=False, primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id', ondelete='CASCADE'), nullable=False, primary_key=True)


class DishCategory(Base):
    __tablename__ = 'dish_category'

    dish_id = Column(Integer, ForeignKey('dish.id', ondelete='CASCADE'), nullable=False, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'), nullable=False, primary_key=True)


Base.metadata.create_all(bind=engine)
