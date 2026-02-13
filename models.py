from pydantic import BaseModel
from pydantic import ConfigDict
from database import Base

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

    class BookResponse(BookBase):
        model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     from_attributes = True
