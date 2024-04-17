from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from typing import Annotated

import book_management.services.services as services
from book_management.schema.book import BookSchema, CheckBook
from book_management.schema.user import UserSchema
from book_management.login import manager


router = APIRouter(prefix="/books" , tags=["Books"])
templates = Jinja2Templates(directory="templates")

@router.get('/all')
def get_all_books(request: Request, user: UserSchema = Depends(manager.optional)):
    books = services.get_all_books()
    count = services.get_number_of_books()
    return templates.TemplateResponse(
        request,
        "book/books.html",
        context={'books': books, 'count': count, 'active_user': user}
    )

@router.get('/add')
def ask_to_add_new_book(request: Request):
    return templates.TemplateResponse(
        "book/new_book.html",
        context={'request': request}
    )

@router.post('/add')
def add_new_book(name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()], price: Annotated[str, Form()], owner_email: Annotated[str, Form()]):
    new_book = {
        'name': name,
        'id': id,
        'author': author,
        'editor': editor,
        'price': price,
        'owner_email': owner_email,
        'status': 'available'
    }
    try:
        book = BookSchema.model_validate(new_book)
        if CheckBook.check_book(new_book) is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid book!",
            )
    except ValidationError as er: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid book!",
        )
    services.add_book(book)
    return RedirectResponse(url="/books/all", status_code=302)

@router.get('/delete')
def ask_to_delete_book(request: Request):
    return templates.TemplateResponse(
        "book/delete_book.html",
        context={'request': request}
    )

@router.post('/delete')
def delete_book_by_name(book_name: Annotated[str, Form()]):
    updated_book_storage = services.delete_book_by_name(book_name)
    if updated_book_storage is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this NAME!",
        )
    return RedirectResponse(url="/books/all", status_code=302)

@router.get('/edit')
def ask_to_edit_book(request: Request):
    return templates.TemplateResponse(
        "book/edit_book.html",
        context={'request': request}
    )

@router.post('/edit')
def edit(book_name: Annotated[str, Form()], name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()], price: Annotated[str, Form()], owner_email: Annotated[str, Form()], status: Annotated[str, Form()]):
    new_book = {
        'name': name,
        'id': id,
        'author': author,
        'editor': editor,
        'price':price,
        'owner_email':owner_email,
        'status':status
    }
    # if services.get_book_by_name(book_name) == None:    
    #    raise HTTPException(
    #        status_code=status.HTTP_404_NOT_FOUND,
    #        detail="No book found with this NAME!",
    #    )
    try:
        book = BookSchema.model_validate(new_book)
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

@router.post('/sell')
def sell(book_name: Annotated[str, Form()]):
    services.sell_unsell_book(book_name)
    return RedirectResponse(url="/users/mybooks", status_code=302)

@router.post('/change/price')
def sell(book_name: Annotated[str, Form()], price: Annotated[str, Form()]):
    services.change_price(book_name, price)
    return RedirectResponse(url="/users/mybooks", status_code=302)
