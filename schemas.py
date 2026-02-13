# from pydantic import BaseModel

# class BookCreate(BaseModel):
#     title: str
#     author: str
#     price: float
#     published_year: int

# class BookUpdate(BaseModel):
#     title: str
#     author: str
#     price: float
#     published_year: int

# class BookResponse(BookCreate):
#     id: int

#     class Config:
#         from_attributes = True




from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(Base):
    __tablename__ = "book_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    author_id = Column(Integer)
    category_id = Column(Integer)
    price = Column(Float)
    published_year = Column(Integer)