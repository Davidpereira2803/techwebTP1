from sqlalchemy import select

from book_management.database import Session
from book_management.schema.user import UserSchema
from book_management.database import Session
from book_management.sql_models.users import User

def get_user_by_name(name: str):
    for user in database['users']:
        if user['name'] == name:
            return User.model_validate(user)
    return None

def get_user_by_firstname(firstname: str):
    for user in database['users']:
        if user['firstname'] == firstname:
            return UserSchema.model_validate(user)
    return None

def get_user_by_email(email: str):
    with Session() as session:
        statement = select(User)
        users_data = session.scalars(statement).all()
    for user in users_data:
        if user.email == email:
            return user
    return None

def add_user(new_user: User):
    database["users"].append(new_user)
    return new_user

def change_role(admin: User, user: User):
    if admin.role != "admin":
        return database
    new_user = {
        'email': user.email,
        'name': user.name,
        'firstname': user.firstname,
        'password': user.password,
        'role': "admin",
        'access': user.access
    }
    delete_user(user.email)
    add_user(new_user)
    return database

def change_password(user: User, password):
    new_user = {
        'email': user.email,
        'name': user.name,
        'firstname': user.firstname,
        'password': password,
        'role': user.role,
        'access': user.access
    }
    delete_user(user.email)
    add_user(new_user)
    return database

def count_users():
    users = database['users']
    return len(users)

def block_user(user: User):
    new_user = {
        'email': user.email,
        'name': user.name,
        'firstname': user.firstname,
        'password': user.password,
        'role': user.role,
        'access': False
    }
    delete_user(user.email)
    add_user(new_user)
    return database

def unblock_user(user: User):
    new_user = {
        'email': user.email,
        'name': user.name,
        'firstname': user.firstname,
        'password': user.password,
        'role': user.role,
        'access': True
    }
    delete_user(user.email)
    add_user(new_user)
    return database

def delete_user(email: str):
    user_not_found = True 
    users = database["users"]
    for i, user in enumerate(users):
        if user['email'] == email:
            user_not_found = False
            users.pop(i)
    if user_not_found:
        return None
    else:
        return users
    
def revoke_user(user: User):
    new_user = {
        'email': user.email,
        'name': user.name,
        'firstname': user.firstname,
        'password': user.password,
        'role': "client",
        'access': user.access
    }
    delete_user(user.email)
    add_user(new_user)
    return database

def promote_user(user: User):
    new_user = {
        'email': user.email,
        'name': user.name,
        'firstname': user.firstname,
        'password': user.password,
        'role': "admin",
        'access': user.access
    }
    delete_user(user.email)
    add_user(new_user)
    return database