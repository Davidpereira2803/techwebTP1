# TP2
The project is structured like the following:

```
techwebtp1/  
|  
├── book_management/  
|   ├── book/  
|   |   ├── book.py
│   │   └── user.py  
│   ├── routes/  
|   |   ├── routes.py
│   │   └── users_routes.py  
│   ├── services/ 
|   |   ├── services.py 
│   │   └── users_services.py  
|   ├── database.py  
|   ├── login.py
│   └── app.py  
|
├── static/
|   └── style.css
|
├── templates/
|   ├── account/
|   |   ├── account_page.html
|   |   └── dashboard.html
|   ├── authentication/
|   |   ├── create.html
|   |   └── login.html
|   ├── book/
|   |   ├── books.html
|   |   ├── delete_book.html
|   |   ├── edit_book.html
|   |   └── new_book.html
|   ├── errors/
|   |   ├── 400.html
|   |   ├── 401.html
|   |   ├── 404.html
|   |   └── 422.html
|   ├── empty_page.html
|   ├── home.html
|   └── my_macro.html
|
├── main.py  
├── README.md  
└── requirements.txt  
```

# Routes
## Voila les routes HTTP du projet des livres:
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
## Voila les routes HTTP du projet des utilisateurs:
```
GET:
    -> '/me'
        -> current_user_route(user: User = Depends(manager))
    -> '/login'
        -> ask_to_login(request: Request)
    -> '/create'
        -> ask_to_create_account(request: Request)
    -> '/home'
        -> ask_to_go_home(request: Request)
    -> '/change'
        -> ask_to_change_password(request: Request)
    -> '/dashboard'
        -> ask_to_dashboard(request: Request)
POST:
    -> '/login'
        -> login_route(email: Annotated[str, Form()],password: Annotated[str, Form()])
    -> '/logout'
        -> logout_route()
    -> '/create'
        -> create_account(email: Annotated[str, Form()],name: Annotated[str, Form()], firstname: Annotated[str, Form()], password: Annotated[str, Form()], password_check: Annotated[str, Form()])
    -> '/change'
        -> change_password(password: Annotated[str, Form()], user: User = Depends(manager.optional))
    -> '/block'
        -> block_user(email: Annotated[str, Form()])
    -> '/unblock'
        -> unblock_user(email: Annotated[str, Form()])
    -> '/promote'
        -> promote(email: Annotated[str, Form()])
    -> '/revoke'
        -> revoke(email: Annotated[str, Form()])
```   
# Functions related to the routes
## Voici les fonctions des routes(GET,POST) pour les livres
```
# Get tout les livres dans la librairie
# Parameter: /
def get_all_books()

# Demande pour ajouter un nouveau livre
# Parameter: request
ask_to_add_new_book(request: Request)

# Ajouter un nouveau livre
# Parameter: name, id, author, editor 
def add_new_book(name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])

# Demande pour effacer un livre
# Parameter: request
ask_to_delete_book(request: Request)

# Effacer un livre
# Parameter: book_name 
def delete_book_by_name(book_name: Annotated[str, Form()])

# Demande pour editer un livre
# Parameter: request
ask_to_edit_book(request: Request)

# Editer un livre de la librarie avec le nom du parametre book_name
# Parameter: book_name, name, id, author, editor
def edit(book_name: Annotated[str, Form()], name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])
```

## Voici les fonctions des routes(GET,POST) pour les livres
```
# Get tout les livres dans la librairie
# Parameter: /
def get_all_books()

# Demande pour ajouter un nouveau livre
# Parameter: request
ask_to_add_new_book(request: Request)

# Ajouter un nouveau livre
# Parameter: name, id, author, editor 
def add_new_book(name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])

# Demande pour effacer un livre
# Parameter: request
ask_to_delete_book(request: Request)

# Effacer un livre
# Parameter: book_name 
def delete_book_by_name(book_name: Annotated[str, Form()])

# Demande pour editer un livre
# Parameter: request
ask_to_edit_book(request: Request)

# Editer un livre de la librarie avec le nom du parametre book_name
# Parameter: book_name, name, id, author, editor
def edit(book_name: Annotated[str, Form()], name: Annotated[str, Form()], id: Annotated[str, Form()], author: Annotated[str, Form()], editor: Annotated[str, Form()])
```

# Functions related to the services
```
# Get tout les livres de la database et return une liste de livre
# Parameter: /
get_all_books() -> list[Book]:

# Compter le nombre de livres dans la database et return un String avec le nombre
# Parameter: /
get_number_of_books():

# Ajouter un nouveau livre à la database
# Parameter: new_book
add_book(new_book: Book):

# Effacer un livre avec le nom passer comme parametre
# Parameter: name
delete_book_by_name(name: str):

# Effacer le livre avec le nom passer comme parametre, et ajouter le avec le nouveau livre passer comme paramtre
# Parameter: book_to_edit, book
edit_book(book_to_edit: str, book: Book):

# Get le livre avec le nom passer comme paramtere
# Parameter: book_name
get_book_by_name(book_name: str):
```

# Templates

Le projet a un fichier 'styles.css' pour styler les templates HTML, deplus on utilise BOOTSTRAP aussi pour le style. Le site est divise en 9 fichier html, ou 3 sont des pages d'erreurs.


```
## books.html

Contient le skeleton de la database de la librairie 

## delete_book.html

Contient le skeleton de la function d'effacer, avec une entree text pour le nom du livre à effacer

## edit_book.html

Contient le skeleton pour la fonction edit, avec une entree text pour le nom du livre à editer et les entrees pour le nouveu livre

## new_book.html

Contient le skeleton de la fonction add, avec les entrees text pour le nouveau livre

## empty_page.html

Contient le skeleton HTML du site

## my_macro.html

Contient le macro pour show_book et show_book_count, pour montrer les valeurs des livres dans la database et le nombre de livres dans la database

## 400.html

Contient le skeleton pour la page d'erreur: 400 Error -- Bad Request page

## 404.html

Contient le skeleton pour la page d'erreur: 404 Error -- Not Found

## 422.html

Contient le skeleton pour la page d'erreur: 422 Error -- Unprocessable Entity

```

# Description

## First Iteration

Le programme nous donne la possibilite d'acceder aux livres de la librairie ('/all'), de compter le nombres des livres dans la librairie ('/count'). On peut aussi ajouter des livres ('/add'), effacer des livres ('/delete/book_name') et d'editer des livres ('/edit/book_name')

Le programme nous returne des erreurs HTTP si les parametres sont faux ou pose de problemes. Par exemple si on veut effacer ou editer un livre qui n'est pas dans la librairie.

## Second Iteration

Cette version du programme est une nouvelle iteration du TP1, toutes les fonctionalitees sont reprises, mais legerement modifier. La partie principale de cette iteration sont les templates HTML, pour avoir une interface HTML pour voir, ajouter, effacer,.., les livres au lieu d'avoir que du JSON. On a des buttons pour interagir avec les pages et des pages d'erreurs en cas d'erreurs.
