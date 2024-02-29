# TP1
The project is structure like the following:

```
techwebtp1/  
|  
├── book_management/  
|   ├── book/  
│   │   └── book.py  
│   ├── routes/  
│   │   └── routes.py  
│   ├── services/  
│   │   └── services.py  
|   ├── database.py  
│   └── app.py  
│  
├── main.py  
├── README.md  
└── requirements.txt  
```

# Routes
These are the HTTP routes used for the functions of the project:
```
GET:
    -> '/all'
        -> get_all_books()
    -> '/count'
        -> get_book_count()
POST:
    -> '/add'
        -> add_new_book(name: str, id, author: str, editor: str)
    -> '/delete/name'
        -> delete_book_by_name(book_name: str)
    -> '/delete/book'
        -> delete_book(name, id, author, editor)
    -> '/edit'
        -> edit(book_name: str, name, id, author, editor)
```    
# Functions
```
# Get all books in the library
# Parameter: /
def get_all_books()

# Get the number of books currently in the library
# Parameter: /
def get_book_count()

# Add a new book to the library
# Parameter: name, id, author, editor -> from the book to add
def add_new_book(name: str, id, author: str, editor: str)

# delete a book from the library by the name
# Parameter: name-> from the book to delete
def delete_book_by_name(book_name: str)

# delete a book from the library 
# Parameter: name, id, author, editor -> from the book to delete
def delete_book(name, id, author, editor)

# edit an existing book from the library
# Parameter: book_name -> from book to edit, {name, id, author, editor} -> new parameters of the book
def edit(book_name: str, name, id, author, editor)

```