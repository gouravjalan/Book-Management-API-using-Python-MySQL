from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from database import Base

from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Book Management API")

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() 

#add a book
@app.post("/books/", response_model=models.BookResponse)
def add_book(book: models.BookCreate, user_id: int, db: Session = Depends(get_db)):
    admin_required(user_id,db)
    result = crud.create_book(db, book) #call crud function
    #check if duplicates
    if isinstance(result,dict) and result.get("error"):
        raise HTTPException(status_code=400,detail=result["error"])

    return result

#get all books
@app.get("/books/", response_model=list[models.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return crud.get_all_books(db)

#get a single book
@app.get("/books/{book_id}", response_model=models.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

#update a book
@app.put("/books/{book_id}", response_model=models.BookResponse)
def update_book(book_id: int, book: models.BookUpdate, user_id: int, db: Session = Depends(get_db)):
    admin_required(user_id,db)
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

#delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_required(user_id,db)
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}



# ---------------- USERS ----------------

@app.post("/users/", response_model=models.UserResponse)
def add_user(user: models.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/users/", response_model=list[models.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)


@app.get("/users/{user_id}", response_model=models.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


#admin dependancy function
def admin_required(user_id: int,db: Session):
    user = db.query(schemas.User).filter(schemas.User.user_id == user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail = "User not found")

    # if user.role.lower != "admin":
        #raise HTTPException(status_code=403, detail= "Only admin can perform this action")

    if user.role.strip().lower() != "admin":
        raise HTTPException(status_code=403, detail="Only admin can perform this action")

    return user


@app.post("/signup")
def signup(user: models.UserSignup,db: Session = Depends(get_db)):
    new_user = crud.create_user(db,user)

    if not new_user:
        raise HTTPException(status_code=400,detail = "Username already exists")
    return {"message":"User created Successfully"}

@app.post("/signin")
def signin(user: models.UserSignin,db: Session = Depends(get_db)):
    existing_user = crud.authenticate_user(db,user)

    if not existing_user:
        raise HTTPException(status_code=401, detail = "Invalid Username or password")
                            
    return {
        "message":"Login Successful",
        "user_id": existing_user.user_id,
        "role": existing_user.role
    }