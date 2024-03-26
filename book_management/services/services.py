from http.client import HTTPException
from pydantic import ValidationError

from book_management.database import database
from book_management.book.book import Book, CheckBook

def get_all_books() -> list[Book]:
    books_dict = database["books"]
    try:
        books  = [Book.model_validate(data) for data in books_dict]
        for book in books_dict:
            CheckBook.check_book(book)
    except ValidationError as er:
        return er
    return books

def get_number_of_books():
    books_dict = database["books"]
    try:
        books  = [Book.model_validate(data) for data in books_dict]
        for book in books_dict:
            CheckBook.check_book(book)
    except ValidationError as er:
        return er
    length = len(books)
    if length == 0:
        return f'The shelf is empty!'
    elif length == 1:
        return f'There is {length} book on the shelf!'
    return f'There are {length} books on the shelf!'

def add_book(new_book: Book):
    database["books"].append(new_book)
    return new_book

def delete_book_by_name(name: str):
    book_not_found = True 
    books = database["books"]
    for i, book in enumerate(books):
        if book['name'] == name:
            book_not_found = False
            books.pop(i)
    if book_not_found:
        return None
    else:
        return books
    
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