from sqlalchemy.orm import Session
from models import BookCreate, BookUpdate,UserCreate
from schemas import Book,User
from auth_utils import hash_password, verify_password


# ------------------ BOOK CRUD ------------------

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



# ------------------ USER CRUD ------------------

def create_user(db: Session, user: UserCreate):
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user

#---------------to create and authenticate user------

def create_user(db,user):
    existing_user = db.query(User).filter(User.username == user.username).first()

    if existing_user:
        return None
    
    hashed_pw = hash_password(user.password)

    new_user = User(
        username = user.username,
        password = hashed_pw,
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)


def authenticate_user(db,user):
    existing_user = db.query(User).filter(User.username == user.username).first()

    if not existing_user:
        return None
    
    if not verify_password(user.password, existing_user.password):
        return None
    
    return existing_user