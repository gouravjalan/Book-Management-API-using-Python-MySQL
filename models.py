from pydantic import BaseModel
from pydantic import ConfigDict
from database import Base
from datetime import date

class BookBase(BaseModel):
    title: str
    author_id: int
    category_id: int
    published_year: int
    price: float
	
class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# class Config:
    #     from_attributes = True


class UserBase(BaseModel):
    role: str
    issue_date: date
    renew_date: date
    book_id: int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int
    model_config = ConfigDict(from_attributes=True)

class UserSignup(BaseModel):
    username : str
    password : str
    role : str 
    #admin or user

class UserSignin(BaseModel):
    username : str
    password : str