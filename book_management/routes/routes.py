from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

import book_management.services.services as services

router = APIRouter(prefix="/books" , tags=["Books"])

@router.get('/')
def get_all_books():
    books = services.get_all_books_amount()
    return JSONResponse(
        content = books,
        status_code = 200
    )

@router.post('/')
def add_new_book(name: str, id, autor: str, editor: str):
    '''
    try:
        if(name):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Invalid name"
            )

    
    catch:
'''