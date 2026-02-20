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
from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "book_table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    author_id = Column(Integer)
    category_id = Column(Integer)
    price = Column(Float)
    published_year = Column(Integer)

class User(Base):
    __tablename__ = "user_table"

    user_id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50), nullable=False)
    issue_date = Column(Date, nullable=False)
    renew_date = Column(Date, nullable=False)
    book_id = Column(Integer, ForeignKey("book_table.id"))
    username = Column(String(100),unique=True,index=True)
    password = Column(String(255))
    book = relationship("Book")
