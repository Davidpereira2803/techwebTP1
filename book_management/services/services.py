from http.client import HTTPException
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from book_management.database import Session
from book_management.schema.book import BookSchema, CheckBook
from book_management.sql_models.books import Book

def access_db():
    with Session() as session:
        statement = select(Book)
        books_data = session.scalars(statement).all()
    return books_data


def get_all_books() -> list[Book]:
    books_data = access_db()
    return [Book(
        name= book.name,
        id=book.id,
        author=book.author,
        editor=book.editor
    )
    for book in books_data
    ]

def get_number_of_books():
    books_data = access_db()
    length = len(books_data)
    if length == 0:
        return f'The shelf is empty!'
    elif length == 1:
        return f'There is {length} book on the shelf!'
    return f'There are {length} books on the shelf!'

def add_book(new_book: BookSchema):
    with Session() as session:
        book = Book(name= new_book.name,
                    id= new_book.id,
                    author= new_book.author,
                    editor=new_book.editor)
        session.add(book)
        session.commit()
    return book

def delete_book_by_name(delete_name: str):
    with Session() as session:
        statement = select(Book).filter_by(name=delete_name)
        user = session.scalars(statement).one()

        session.delete(user)
        session.commit()
    
def edit_book(book_to_edit: str, book: Book):
    delete_book_by_name(book_to_edit)
    add_book(book.model_dump())
    return database

def get_book_by_name(book_name: str):
    books = database["books"]
    for book in books:
        if book['name'] == book_name:
            return book
    return None