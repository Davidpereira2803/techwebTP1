from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

import book_management.services.services as services
from book_management.book.book import Book, CheckBook


router = APIRouter(prefix="/books" , tags=["Books"])

@router.get('/all')
def get_all_books():
    books = services.get_all_books()
    return JSONResponse(
        content=[book.model_dump() for book in books],
        status_code = 200
    )

@router.get('/count')
def get_book_count():
    count = services.get_number_of_books()
    return JSONResponse(
        content = count,
        status_code = 200
    )

@router.post('/add')
def add_new_book(name: str, id, author: str, editor: str):
    new_book = {
        'name': name,
        'id': id,
        'author': author,
        'editor': editor,
    }
    services.add_book(new_book)
    return JSONResponse(new_book)

@router.post('/delete/name')
def delete_book_by_name(book_name: str):
    updated_book_storage = services.delete_book_by_name(book_name)
    return JSONResponse(updated_book_storage)

@router.post('/delete/book')
def delete_book(name, id, author, editor):
    data = {
        'name': name,
        'id': id,
        'author': author,
        'editor': editor
    }
    try:
        book_to_delete  = [Book.model_validate(data)]
        CheckBook.check_book(data)
    except ValidationError as er:
        return er
    updated_book_storage = services.delete_book(book_to_delete)
    return JSONResponse(updated_book_storage)

@router.post('/edit')
def edit(book_name: str, name, id, autor, editor):
    services.edit_book(services.book_to_edit(book_name), name, id, autor, editor)
    return JSONResponse(services.book_storage)
    
