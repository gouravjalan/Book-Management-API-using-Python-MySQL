from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base

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
def add_book(book: models.BookCreate, db: Session = Depends(get_db)):
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
def update_book(book_id: int, book: models.BookUpdate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

#delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}



 