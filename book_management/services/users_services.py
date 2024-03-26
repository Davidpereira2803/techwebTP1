from book_management.database import book_storage
from book_management.book.user import User

def get_user_by_name(name: str):
    for user in book_storage['users']:
        if user['name'] == name:
            return User.model_validate(user)
    return None

def get_user_by_firstname(firstname: str):
    for user in book_storage['users']:
        if user['firstname'] == firstname:
            return User.model_validate(user)
    return None

def get_user_by_email(email: str):
    for user in book_storage['users']:
        if user['email'] == email:
            return User.model_validate(user)
    return None

def add_user(new_user: User):
    book_storage["users"].append(new_user)
    return new_user

def change_role(admin: User, user: User):
    if admin.role != "admin":
        return book_storage
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
    return book_storage

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
    return book_storage

def count_users():
    users = book_storage['users']
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
    return book_storage

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
    return book_storage

def delete_user(email: str):
    user_not_found = True 
    users = book_storage["users"]
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
    return book_storage

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
    return book_storage