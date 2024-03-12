# TP2
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
|
├── static/
|   └── style.css
|
├── templates/
|   └── errors/
|   |   ├── 400.html
|   |   ├── 404.html
|   |   └── 422.html
│   ├── books.html
|   ├── delete_book.html
|   ├── edit_book.html
|   ├── empty_page.html
|   ├── my_macro.html
|   └── new_book.html
|
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
    -> '/add'
        -> ask_to_add_new_book(request: Request)
    -> '/delete'
        -> ask_to_delete_book(request: Request)
    -> '/edit'
        -> ask_to_edit_book(request: Request)
POST:
    -> '/add'
        -> add_new_book(name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])
    -> '/delete'
        -> delete_book_by_name(book_name: Annotated[str, Form()])
    -> '/edit'
        -> edit(book_name: Annotated[str, Form()], name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])
```    
# Functions related to the routes
These are the functions related to the routes(GET,POST)
```
# Get all books in the library
# Parameter: /
def get_all_books()

# Request to add new book
# Parameter: request
ask_to_add_new_book(request: Request)

# Add a new book to the library
# Parameter: name, id, author, editor 
def add_new_book(name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])

# Request to delete a book
# Parameter: request
ask_to_delete_book(request: Request)

# delete a book from the library by the name
# Parameter: book_name 
def delete_book_by_name(book_name: Annotated[str, Form()])

# Request to edit a book
# Parameter: request
ask_to_edit_book(request: Request)

# edit an existing book from the library
# Parameter: book_name, name, id, author, editor
def edit(book_name: Annotated[str, Form()], name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])
```

# Functions related to the services
```
# Get all books in the database and return a list of Book
# Parameter: /
get_all_books() -> list[Book]:

# Count the number of books in the database and return a text with the number
# Parameter: /
get_number_of_books():

# Append a new book to the database
# Parameter: new_book
add_book(new_book: Book):

# Delete a book with the given name passed as parameter
# Parameter: name
delete_book_by_name(name: str):

# Edit the book with the given name passed as parameter, replace it with the new book passed as parameter
# Parameter: book_to_edit, book
edit_book(book_to_edit: str, book: Book):

# Get the book that matches the parameter and return it
# Parameter: book_name
get_book_by_name(book_name: str):
```

# Templates

The project has a file 'styles.css' to style the HTMl templates, but it also uses BOOTSTRAP for the styling. The site is divided into 9 html files, where 3 of them are error pages. 

## books.html

Contains the skeleton of the library database

## delete_book.html

Contains the skeleton of the delete function, with one textfield for the book name to delete

## edit_book.html

Contains the skeleton of the edit function, with one textfield for the book name to edit and the textfields to input the new version of the book

## new_book.html

Contains the skeleton of the add function, with the textfields to input the new book

## empty_page.html

Contains the HTML skeleton of the site

## my_macro.html

Contains the macro for show_book and show_book_count, to display the values of the books in the database, and the number of books in the database

## 400.html

Contains the skeleton of the 400 Error -- Bad Request page

## 404.html

Contains the skeleton of the 404 Error -- Not Found

## 422.html

Contains the skeleton of the 422 Error -- Unprocessable Entity

# Description

## First Iteration

The program allows one to get all the books in the library ('/all'), to get the number of books in the library ('/count').
Next, it allows to add new books to the library ('/add'), to delete existing books from the library ('/delete/book_name') and to edit existing books from the library ('/edit/book_name').

The program gives some HTTP errors if the parameters are wrong or if for instance one wants to delete or edit a book that is not in the library.

## Second Iteration

This version of the program is a further iteration of TP1, thus all these functionalities still remain, but where slightly modified. The main new part of this iteration are the HTML templates, that actually show the library in form of HTML instead of JSON. The site has buttons to add, delete and edit the books in the library and also includes some error pages, such as the 400, 404 and 422 error page. 
