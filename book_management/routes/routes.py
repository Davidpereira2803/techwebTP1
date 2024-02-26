from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

import book_management.services.services as services

router = APIRouter(prefix="/books" , tags=["Books"])

@router.get('/all')
def get_all_books():
    books = services.get_all_books()
    return JSONResponse(
        content = books,
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
def add_new_book(name: str, id, autor: str, editor: str):
    new_book = {
        'name': name,
        'id': id,
        'autor': autor,
        'editor': editor,
    }
    try:
        if(name == '' or autor == '' or editor == ''):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Invalid name or autor or editor!"
            )
        elif(name.isspace() or autor.isspace() or editor.isspace()):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Invalid name or autor or editor!"
            )
    except HTTPException as er:
        return er
    else:
        services.add_book(new_book)
        return JSONResponse(new_book)

@router.post('/delete')
def delete_book_by_name(book_name: str):
    new_book_storage = services.delete_book(book_name)
    return JSONResponse(new_book_storage)

@router.post('/edit')
def edit(book_name: str, name, id, autor, editor):
    services.edit_book(services.book_to_edit(book_name), name, id, autor, editor)
    return JSONResponse(services.book_storage)
    
