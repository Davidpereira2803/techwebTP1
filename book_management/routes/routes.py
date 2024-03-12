from fastapi import APIRouter, HTTPException, status, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from typing import Annotated

import book_management.services.services as services
from book_management.book.book import Book, CheckBook


router = APIRouter(prefix="/books" , tags=["Books"])
templates = Jinja2Templates(directory="templates")

@router.get('/all')
def get_all_books(request: Request):
    books = services.get_all_books()
    count = services.get_number_of_books()
    return templates.TemplateResponse(
        "books.html",
        context={'request': request, 'books': books, 'count': count}
    )

@router.get('/count')
def get_book_count():
    count = services.get_number_of_books()
    return JSONResponse(
        content = count,
        status_code = 200
    )

@router.get('/add')
def ask_to_add_new_book(request: Request):
    return templates.TemplateResponse(
        "new_book.html",
        context={'request': request}
    )

@router.post('/add')
def add_new_book(name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()]):
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
    services.add_book(book.model_dump())
    return RedirectResponse(url="/books/all", status_code=302)

@router.get('/delete')
def ask_to_delete_book(request: Request):
    return templates.TemplateResponse(
        "delete_book.html",
        context={'request': request}
    )

@router.post('/delete')
def delete_book_by_name(book_name: Annotated[str, Form()]):
    updated_book_storage = services.delete_book_by_name(book_name)
    if updated_book_storage is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this NAME!",
        )
    return RedirectResponse(url="/books/all", status_code=302)

@router.get('/edit')
def ask_to_edit_book(request: Request):
    return templates.TemplateResponse(
        "edit_book.html",
        context={'request': request}
    )

@router.post('/edit')
def edit(book_name: Annotated[str, Form()], name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()]):
    new_book = {
        'name': name,
        'id': id,
        'author': author,
        'editor': editor
    }
    if services.get_book_by_name(book_name) == None:    
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this NAME!",
        )
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
    services.edit_book(book_name, book)
    return RedirectResponse(url="/books/all", status_code=302)


    
