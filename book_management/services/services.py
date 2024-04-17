from http.client import HTTPException
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from book_management.database import Session
from book_management.schema.book import BookSchema, CheckBook
from book_management.sql_models.books import Book
from book_management.sql_models.users import User

def access_db():
    with Session() as session:
        statement = select(Book)
        books_data = session.scalars(statement).all()
    return books_data

def get_users_db():
    with Session() as session:
        statement = select(User)
        users_data = session.scalars(statement).all()
    return users_data


def get_all_books() -> list[Book]:
    books_data = access_db()
    return [Book(
        name= book.name,
        id=book.id,
        author=book.author,
        editor=book.editor,
        price=book.price,
        owner_email=book.owner_email,
        status=book.status
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
                    editor=new_book.editor,
                    price=new_book.price,
                    owner_email=new_book.owner_email,
                    status= new_book.status)
        session.add(book)
        session.commit()
    get_owner_names()
    return book

def delete_book_by_name(delete_name: str):
    with Session() as session:
        statement = select(Book).filter_by(name=delete_name)
        user = session.scalars(statement).one()

        session.delete(user)
        session.commit()
    
def edit_book(book_to_edit: str, book: BookSchema):
    with Session() as session:
        statement = select(Book).filter_by(name= book_to_edit)
        new_book = session.scalars(statement).one()

        new_book.name = book.name
        new_book.id = book.id
        new_book.author = book.author
        new_book.editor = book.editor
        new_book.price = book.price
        new_book.owner_email = book.owner_email
        new_book.status = book.status

        session.commit()


def get_owner_names():
    name = []
    books = access_db()
    users = get_users_db()

    for book in books:
        for user in users:
            if book.owner_email == user.email:
                name.append(user.name)
    return name

def get_owner_firstnames():
    firstname = []
    books = access_db()
    users = get_users_db()

    for book in books:
        for user in users:
            if book.owner_email == user.email:
                firstname.append(user.firstname)
    return firstname

def sell_unsell_book(book_name:str):
    with Session() as session:
        statement = select(Book).filter_by(name= book_name)
        new_book = session.scalars(statement).one()

        if new_book.status == "sold":
            new_book.status = "available"
        else:
            new_book.status = "sold"

        session.commit()

def change_price(book_name:str, price:str):
    with Session() as session:
        statement = select(Book).filter_by(name= book_name)
        new_book = session.scalars(statement).one()
        
        new_book.price = price

        session.commit()