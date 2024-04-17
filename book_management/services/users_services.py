from sqlalchemy import select

from book_management.database import Session
from book_management.schema.user import UserSchema
from book_management.database import Session
from book_management.sql_models.users import User

def access_db():
    with Session() as session:
        statement = select(User)
        users_data = session.scalars(statement).all()
    return users_data

def get_user_by_name(search_name: str):
    with Session() as session:
        statement = select(User).filter_by(name=search_name)
        user = session.scalars(statement).first()

    return UserSchema.model_validate(user)

def get_user_by_firstname(search_firstname: str):
    with Session() as session:
        statement = select(User).filter_by(firstnamename=search_firstname)
        user = session.scalars(statement).first()

    return UserSchema.model_validate(user)

def get_user_by_email(email: str):
    with Session() as session:
        statement = select(User)
        users_data = session.scalars(statement).all()
    for user in users_data:
        if user.email == email:
            return user
    return None

def add_user(new_user: UserSchema):
    with Session() as session:
        user = User(email= new_user.email,
                    name= new_user.name,
                    firstname= new_user.firstname,
                    password= new_user.password,
                    role= new_user.role,
                    access= new_user.access)
        session.add(user)
        session.commit()

    return user

def change_role(user: UserSchema):
    with Session() as session:
        statement = select(User).filter_by(name=user.name)
        edit_user = session.scalars(statement).one()

        edit_user.role = "admin"

        session.commit()

def change_password(user: UserSchema, password, check_password):
    if password == check_password:
        with Session() as session:
            statement = select(User).filter_by(name=user.name)
            edit_user = session.scalars(statement).one()

            edit_user.password = password

            session.commit()

def change_information(user: UserSchema, email, firstname, name):
    with Session() as session:
        statement = select(User).filter_by(name=user.name)
        edit_user = session.scalars(statement).one()

        edit_user.email = email
        edit_user.name = name
        edit_user.firstname = firstname

        session.commit()

def count_users():
    users = access_db()
    return len(users)

def block_user(user: UserSchema):
    with Session() as session:
        statement = select(User).filter_by(name=user.name)
        edit_user = session.scalars(statement).one()

        edit_user.access = False

        session.commit()

def unblock_user(user: User):
    with Session() as session:
        statement = select(User).filter_by(name=user.name)
        edit_user = session.scalars(statement).one()

        edit_user.access = True

        session.commit()

def delete_user(email: str):
    with Session() as session:
        statement = select(User).filter_by(email=email)
        user = session.scalars(statement).one()

        session.delete(user)
        session.commit()
    
def revoke_user(user: UserSchema):
    with Session() as session:
        statement = select(User).filter_by(name=user.name)
        edit_user = session.scalars(statement).one()

        edit_user.role = "client"

        session.commit()

def promote_user(user: UserSchema):
    with Session() as session:
        statement = select(User).filter_by(name=user.name)
        edit_user = session.scalars(statement).one()

        edit_user.role = "admin"

        session.commit()