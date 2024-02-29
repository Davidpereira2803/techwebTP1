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
    try:
        book = Book.model_validate(new_book)
        if CheckBook.check_book(new_book) is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid book!",
            )
    except ValidationError: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid book!",
        )
    services.add_book(new_book)
    return JSONResponse(book.model_dump())

@router.post('/delete/{book_name}')
def delete_book_by_name(book_name: str):
    updated_book_storage = services.delete_book_by_name(book_name)
    if updated_book_storage is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this NAME!",
        )
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
        Book.model_validate(data)
        CheckBook.check_book(data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid book!",
        )
    updated_book_storage = services.delete_book(data)
    if updated_book_storage is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No such book found!",
        )
    return JSONResponse(updated_book_storage)

@router.post('/edit/{book_name}')
def edit(book_name: str, name, id, author, editor):
    new_book = {
        'name': name,
        'id': id,
        'author': author,
        'editor': editor
    }
    if services.get_book_by_name(book_name) == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No book found with this NAME!",
        )
    try:
        book = Book.model_validate(new_book)
        if CheckBook.check_book(new_book) is None:
            print(f'{new_book["author"]},{new_book["name"]},{new_book["id"]},{new_book["editor"]}')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid bookh!",
            )
    except ValidationError: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid book!",
        )
    update = services.edit_book(book_name, new_book)
    return JSONResponse(update)
    
