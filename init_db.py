from typing import Optional
from sqlalchemy import ForeignKey, create_engine, String, Boolean, Delete
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    email= mapped_column(String(72), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(72))
    firstname: Mapped[str] = mapped_column(String(72))
    password: Mapped[str] = mapped_column(String(72))
    role: Mapped[str] = mapped_column(String(72))
    access: Mapped[bool] = mapped_column(Boolean)

    #books: Mapped[list["Book"]] = relationship()

class Book(Base):
    __tablename__ = "books"

    name = mapped_column(String(72))
    id = mapped_column(String(72), primary_key=True, unique= True)
    author = mapped_column(String(72))
    editor : Mapped[Optional[str]] = mapped_column(String(72), nullable=True)
    #price = mapped_column(String(72))

    #owner_email: Mapped[str] = mapped_column(ForeignKey("users.email"))
    #user: Mapped["User"] = relationship()


def init_db():
    engine = create_engine('sqlite:///data/db.sqlite')
    Base.metadata.create_all(engine)
    
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session = Session()
    
    try:
        session.query(User).delete()
        session.query(Book).delete()
        
        default_users = [
            User(email='admin', name='admin', firstname='admin', password='admin', role='admin', access=True),
            User(email='1@email.com', name='1', firstname='1', password='1234', role='user', access=True),
            User(email='2@email.com', name='2', firstname='2', password='1234', role='user', access=False),
        ]

        default_books = [
            Book(name="1",id="1",author="1",editor="1"),
            Book(name="Structure and Interpretation of Computer Programs", id= '978-0262510875', author= "Harold Abelson, Gerald Jay Sussman and Julie Sussman", editor= 'MIT Press'),
            Book(name= "Introduction to Algorithms", id= '978-0262510855', author= "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein", editor= 'MIT Press'),
            Book(name= "Design Patterns: Elements of Reusable Object-Oriented Software", id= '978-0201633610', author= "Erich Gamma, Richard Helm, Ralph Johnson, et John Vlissides", editor= 'Addison-Wesley Professional')
        ]
        
        session.add_all(default_users)
        session.add_all(default_books)
        
        session.commit()
        print("Database initialized with default values.")
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == '__main__':
    init_db()
