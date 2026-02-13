from sqlalchemy.orm import Session
from models import BookCreate, BookUpdate
from schemas import Book

def create_book(db: Session, book: BookCreate):
    # Check if book with same title and author already exists
    existing_book = db.query(Book).filter(
        Book.title == book.title,
        Book.author_id == book.author_id
    ).first()

    if existing_book:
        return {"error": "Book already exists"}  # or raise an HTTPException in main.py
    
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_all_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book):
    existing_book = get_book_by_id(db, book_id)
    if not existing_book:
        return None

    for key, value in book.dict().items():
        setattr(existing_book, key, value)

    db.commit()
    db.refresh(existing_book)
    return existing_book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book
