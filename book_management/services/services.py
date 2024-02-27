from http.client import HTTPException
from pydantic import ValidationError

from book_management.database import book_storage
from book_management.book.book import Book, CheckBook

def get_all_books() -> list[Book]:
    try:
        books  = [Book.model_validate(data) for data in book_storage]
        for book in book_storage:
            CheckBook.check_book(book)
    except ValidationError as er:
        return er
    return books

def get_number_of_books():
    try:
        books  = [Book.model_validate(data) for data in book_storage]
        for book in book_storage:
            CheckBook.check_book(book)
    except ValidationError as er:
        return er
    length = len(books)
    if length == 0:
        return f'The shelf is empty!'
    elif length == 1:
        return f'There is {length} book on the shelf!'
    return f'There are {length} books on the shelf!'

def get_book_by_name(book_name: str):
    for book in book_storage:
        if book['name'] == book_name:
            return book
    return None

def add_book(new_book):
    book_storage.append(new_book)
    return new_book

def delete_book_by_name(name: str):
    book_not_found = True 
    for i, book in enumerate(book_storage):
        if book['name'] == name:
            book_not_found = False
            book_storage.pop(i)
    if book_not_found:
        return None
    else:
        return book_storage

def delete_book(book_to_delete: Book):
    book_not_found = True
    for i, book in enumerate(book_storage):
        if book == book_to_delete:
            book_not_found = False
            book_storage.pop(i)
    if book_not_found:
        return None
    else:
        return book_storage

def edit_book(book_to_edit: str, book):
    delete_book_by_name(book_to_edit)
    add_book(book)
    return book_storage  