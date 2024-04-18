from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(
    "sqlite:///data/db.sqlite",
    echo=True,
)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

from book_management.sql_models.books import Book
from book_management.sql_models.users import User

def create_database():
    Base.metadata.create_all(engine)

def delete_database():
    Base.metadata.clear()

"""
database = {
    "books": [
        {
            "name": "Structure and Interpretation of Computer Programs",
            "id": '978-0262510875',
            "author": "Harold Abelson, Gerald Jay Sussman and Julie Sussman",
            "editor": 'MIT Press',
        },
        {
            "name": "Introduction to Algorithms",
            "id": '978-0262510875',
            "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein",
            "editor": 'MIT Press',
        },
        {
            "name": "Design Patterns: Elements of Reusable Object-Oriented Software",
            "id": '978-0201633610',
            "author": "Erich Gamma, Richard Helm, Ralph Johnson, et John Vlissides",
            "editor": 'Addison-Wesley Professional',
        },
    ],
    "users":[
        {
            "email": "admin",
            "name":"admin",
            "firstname": "admin",
            "password":"admin",
            "role":"admin",
            "access": True,
        },
        {
            "email": "1@email.com",
            "name":"1",
            "firstname": "11",
            "password":"1234",
            "role":"client",
            "access": True,
        },
        {
            "email": "2@email.com",
            "name":"2",
            "firstname": "22",
            "password":"1234",
            "role":"client",
            "access": False,
        },
    ]
}
"""