# TP1
The project is structured like the following:

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
    -> '/delete/book_name'
        -> delete_book_by_name(book_name: str)
    -> '/edit/book_name'
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
# Parameter: new_book: Book 
def add_new_book(new_book: Book)

# delete a book from the library by the name
# Parameter: name 
def delete_book_by_name(name: str)

# edit an existing book from the library
# Parameter: book_name, book
def edit(book_name: str, book: Book)

# get book by name (Help function)
# Parameter: book_name
def get_book_by_name(book_name: str)

```
# Description

The program allows one to get all the books in the library ('/all'), to get the number of books in the library ('/count').
Next, it allows to add new books to the library ('/add'), to delete existing books from the library ('/delete/book_name') and to edit existing books from the library ('/edit/book_name').

The program gives some HTTP errors if the parameters are wrong or if for instance one wants to delete or edit a book that is not in the library.