from book_management.database import book_storage

def get_all_books():
    return book_storage

def get_number_of_books():
    length = len(book_storage)
    if length == 0:
        return f'The shelf is empty!'
    elif length == 1:
        return f'There is {length} book on the shelf!'
    return f'There are {length} books on the shelf!'

def add_book(new_book):
    book_storage.append(new_book)
    return new_book

def delete_book_by_name(name: str):
    new_book_storage = []
    for book in book_storage:
        if book['name'] != name:
            new_book_storage.append(book)
    return new_book_storage

def delete_book(book):
    new_book_storage = []
    for b in book_storage:
        if b != book:
            new_book_storage.append(b)
    print(new_book_storage)
    return new_book_storage

def book_to_edit(name):
    try:
        for b in book_storage:
            if b['name'] == name:
                return b
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Invalid name or autor or editor!"
            )
    except HTTPException as er:
        return er

def edit_book(book, name: str, id, autor: str, editor: str):
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
    book_storage = delete_book(book)
    new_book = {
        'name': name,
        'id': id,
        'autor': autor,
        'editor': editor
    }
    book_storage = [] # i cannot assign a value to book_storage
    add_book(new_book)
    return book_storage  