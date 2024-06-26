from typing import Annotated

from fastapi import APIRouter, HTTPException, Request, status, Depends, Form, Body
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from book_management.login import manager
import book_management.services.users_services as services
import book_management.services.services as book_services
from book_management.schema.user import UserSchema 
from book_management.database import Session 

login_router = APIRouter(prefix="/users")
templates = Jinja2Templates(directory="templates")

@login_router.get("/me")
def current_user_route(user: UserSchema = Depends(manager)):
    return user

@login_router.get('/login')
def ask_to_login(request: Request):
    return templates.TemplateResponse(
        "authentication/login.html",
        context={'request': request}
    )

@login_router.post('/login')
def login_route(email: Annotated[str, Form()],password: Annotated[str, Form()]):
    user = services.get_user_by_email(email)
    if user is None or user.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Bad credentials!"
        )
    
    if user.access != True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Account blocked!"
        )

    access_token = manager.create_access_token(
        data={'sub': user.email}
    )

    response = RedirectResponse(url="/books/all", status_code=302)
    response.set_cookie(
        key=manager.cookie_name,
        value=access_token,
        httponly=True
    )
    return response

@login_router.post('/logout')
def logout_route():
    response = RedirectResponse(url="/users/home", status_code=302)
    response.delete_cookie(
        key=manager.cookie_name,
        httponly=True
    )
    return response

@login_router.get('/create')
def ask_to_create_account(request: Request):
        return templates.TemplateResponse(
        "authentication/create.html",
        context={'request': request}
    )

@login_router.post('/create')
def create_account(email: Annotated[str, Form()],name: Annotated[str, Form()], firstname: Annotated[str, Form()], password: Annotated[str, Form()], password_check: Annotated[str, Form()]):
    if password != password_check:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Passwords don't match!"
        )
    new_user = {
        'email': email,
        'name': name,
        'firstname': firstname,
        'password': password,
        'role': "client",
        'access': True
    }
    try:
        user = UserSchema.model_validate(new_user)
    except ValidationError as er: 
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Bad credentials!"
        )
    services.add_user(user)
    return RedirectResponse(url="/books/all", status_code=302)

@login_router.get('/home')
def ask_to_go_home(request: Request):
    books = book_services.get_all_books()
    count = book_services.get_number_of_books()
    users = services.access_db()
    return templates.TemplateResponse(
        "home.html",
        context={'request': request,'books': books, 'count': count, 'users': users}
    )

@login_router.get('/change')
def ask_to_change_password(request: Request, user: UserSchema = Depends(manager.optional)):
        return templates.TemplateResponse(
        "account/account_page.html",
        context={'request': request, 'active_user': user}
    )

@login_router.post('/change/password')
def change_password(old_password: Annotated[str, Form()], password: Annotated[str, Form()], check_password: Annotated[str, Form()],user: UserSchema = Depends(manager.optional)):
    if check_password != password or user.password != old_password: 
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Passwords don't match!"
        )
    services.change_password(user, password, check_password)
    return RedirectResponse(url="/books/all", status_code=302)

@login_router.post('/change/information')
def change_information(email: Annotated[str, Form()], name: Annotated[str, Form()],firstname: Annotated[str, Form()],user: UserSchema = Depends(manager.optional)):
    services.change_information(user, email, firstname, name)
    return RedirectResponse(url="/books/all", status_code=302)


@login_router.get('/dashboard')
def ask_to_dashboard(request: Request, user: UserSchema = Depends(manager.optional)):
        users = services.access_db()
        count = services.count_users()
        return templates.TemplateResponse(
        "account/dashboard.html",
        context={'request': request, 'active_user': user, 'users': users, 'count': count}
    )

@login_router.post('/block')
def block_user(email: Annotated[str, Form()]):
     user = services.get_user_by_email(email)
     if user.role == "admin":
        return RedirectResponse(url="/users/dashboard", status_code=302)
     services.block_user(user)
     return RedirectResponse(url="/users/dashboard", status_code=302)

@login_router.post('/unblock')
def unblock_user(email: Annotated[str, Form()]):
     user = services.get_user_by_email(email)
     services.unblock_user(user)
     return RedirectResponse(url="/users/dashboard", status_code=302)

@login_router.post('/promote')
def promote(email: Annotated[str, Form()]):
     user = services.get_user_by_email(email)
     if user.role == "admin":
        return RedirectResponse(url="/users/dashboard", status_code=302)
     services.promote_user(user)
     return RedirectResponse(url="/users/dashboard", status_code=302)

@login_router.post('/revoke')
def revoke(email: Annotated[str, Form()]):
     user = services.get_user_by_email(email)
     services.revoke_user(user)
     return RedirectResponse(url="/users/dashboard", status_code=302)

@login_router.get('/mybooks')
def get_mybooks(request: Request, user: UserSchema = Depends(manager.optional)):
    books = book_services.get_all_books()
    return templates.TemplateResponse(
        "account/my_books.html",
        context={'request': request, 'active_user': user, 'books': books}
    )
     