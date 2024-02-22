from book_management.database import book_storage

def get_all_books():
    return book_storage

def get_number_of_books():
    return len(book_storage)

def add_book(new_book):
    book_storage.append(new_book)
    return new_book

def delete_book(name: str):
    new_book_storage = []
    for book in book_storage:
        print(type(book))
        if book.get('name') != name:
            new_book_storage.append(book)
    return new_book_storage

def edit_book(name: str):
    return


# if already once triggered it will still add and count more books -> to correct
def get_all_books_amount():
    print(delete_book('Book1'))
    add_book(f'There are {str(get_number_of_books())} books in the shelf!')
    return  get_all_books()