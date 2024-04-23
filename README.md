# TP
Le projet est structuré comme ceci:

```
techwebtp1/  
|  
├── book_management/  
|   ├── schema/  
|   |   ├── book.py
│   │   └── user.py  
│   ├── routes/  
|   |   ├── routes.py
│   │   └── users_routes.py  
│   ├── services/ 
|   |   ├── services.py 
│   │   └── users_services.py  
|   ├── sql_models/
|   |   ├── books.py
|   |   └── users.py
|   ├── database.py  
|   ├── login.py
│   └── app.py  
|
|
├── data/
|   └── db.sqlite
|
├── static/
|   └── style.css
|
├── templates/
|   ├── account/
|   |   ├── account_page.html
|   |   ├── dashboard.html
|   |   └── my_books.html
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
    -> '/sell'
        -> sell(book_name: Annotated[str, Form()])
    -> '/change/price'
        -> sell(book_name: Annotated[str, Form()], price: Annotated[str, Form()])

```   
## Voila les routes HTTP du projet des utilisateurs:
```
GET:
    -> '/me'
        -> current_user_route(user: UserSchema = Depends(manager))
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
    -> '/mybooks'
        -> get_mybooks(request: Request, user: UserSchema = Depends(manager.optional))
POST:
    -> '/login'
        -> login_route(email: Annotated[str, Form()],password: Annotated[str, Form()])
    -> '/logout'
        -> logout_route()
    -> '/create'
        -> create_account(email: Annotated[str, Form()],name: Annotated[str, Form()], firstname: Annotated[str, Form()], password: Annotated[str, Form()], password_check: Annotated[str, Form()])
    -> '/change/password'
        -> change_password(password: Annotated[str, Form()], user: UserSchema = Depends(manager.optional))
    -> '/change/information'
        -> change_information(email: Annotated[str, Form()], name: Annotated[str, Form()],firstname: Annotated[str, Form()],user: UserSchema = Depends(manager.optional))
    -> '/block'
        -> block_user(email: Annotated[str, Form()])
    -> '/unblock'
        -> unblock_user(email: Annotated[str, Form()])
    -> '/promote'
        -> promote(email: Annotated[str, Form()])
    -> '/revoke'
        -> revoke(email: Annotated[str, Form()])
```   
# Functions en relation avec les routes
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

# Changer le status du livre avec le nom passer comme parametre
# Parameter: book_name
def sell(book_name: Annotated[str, Form()])

# Changer le prix du livre avec le nom passer comme parametre
# Parameter: book_name, price
def sell(book_name: Annotated[str, Form()], price: Annotated[str, Form()])

```

## Voici les fonctions des routes(GET,POST) pour les utilisateurs
```
# Get l'utilisateur actuel
# Parameter: user
def current_user_route(user: UserSchema = Depends(manager)):

# Demande pour un login
# Parameter: request
def ask_to_login(request: Request):

# Faire le login d'un utilisateur
# Parameter: email, password
def login_route(email: Annotated[str, Form()],password: Annotated[str, Form()]):

# Faire le logout d'un utilisateurs
# Parameter: /
def logout_route():

# Demande pour créer un compte
# Parameter: request 
def ask_to_create_account(request: Request):

# Creation d'un compte
# Parameter: request
def create_account(email: Annotated[str, Form()],name: Annotated[str, Form()], firstname: Annotated[str, Form()], password: Annotated[str, Form()], password_check: Annotated[str, Form()]):

# Demande pour aller sur la page home
# Parameter: request
def ask_to_go_home(request: Request):

# Demande pour changer le password de l'utilisateur actuel
# Parameter: request, user
def ask_to_change_password(request: Request, user: UserSchema = Depends(manager.optional)):

# Changement du password de l'utilisateur actuel
# Parameter: password, user
def change_password(password: Annotated[str, Form()], user: UserSchema = Depends(manager.optional)):

# Changer les informations personnelles du compte ( email, nom, prénom)
# Parameter: email, name, firstname, user
def change_information(email: Annotated[str, Form()], name: Annotated[str, Form()],firstname: Annotated[str, Form()],user: UserSchema = Depends(manager.optional))

# Demande pour aller sur la page dashboard
# Parameter: request, user
def ask_to_dashboard(request: Request, user: UserSchema = Depends(manager.optional)):

# Bloquer un utilisateur
# Parameter: email
def block_user(email: Annotated[str, Form()]):

# Débloquer un utilisateur
# Parameter: email
def unblock_user(email: Annotated[str, Form()]):

# Promouvoir un utilisateur
# Parameter: email
def promote(email: Annotated[str, Form()]):

# Limoger un utilisateur
# Parameter: email
def revoke(email: Annotated[str, Form()]):
```

# Fonctions en relations avec les services
## Pour les livres
```
# Acceder aux livres de la database
# Parameter: /
def access_db():

# Acceder aux utilisateurs de la database
# Parameter: /
def get_users_db():

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

# Changer le status du livre(sold/unavailable) avec le nom passer comme paramètre
# Parameter: book_name
def sell_unsell_book(book_name:str):

# Changer le prix du livre avec le nom passer comme paramètre
# Parameter: book_name
def change_price(book_name:str, price:str):

```

## Pour les utilisateurs
```
# Acceder aux utilisateur de la database
# Parameter: /
def access_db()

# Obtenir un utilisateur par le nom
# Parameter: name
def get_user_by_name(name: str):

# Obtenir un utilisateur par le prénom
# Parameter: firstname
def get_user_by_firstname(firstname: str):

# Obtenir un utilisateur par l'email
# Parameter: email
def get_user_by_email(email: str):

# Ajouter un utilisateur
# Parameter: new_user
def add_user(new_user: User):

# Changer le role d'un utilisateur
# Parameter: user
def change_role(user: UserSchema):

# Changer le password de l'utilisateur avec un controle du password actuel
# Parameter: user, password, check_password
def change_password(user: User, password, check_password):

# Changer les information de l'utilisateur (email, name, firstname)
# Parameter: user, email, firstname, name
def change_information(user: UserSchema, email, firstname, name):

# Compter les utilisateurs dans la database
# Parameter: /
def count_users():

# Bloquer l'utilisateur passer comme paramètre
# Parameter: user
def block_user(user: UserSchema):

# Débloquer l'utilisateur passer comme paramètre
# Parameter: user
def unblock_user(user: UserSchema):

# Promouvoir l'utilisateur passer comme paramètre
# Parameter: user
def promote_user(user: UserSchema):

# Limoger l'utilisateur passer comme paramètre
# Parameter: user
def revoke_user(user: UserSchema):

# Supprimer l'utilisateur avec l'email passer comme paramètre
# Paramter: email
def delete_user(email: str):
```

# Templates

Le projet a un fichier 'styles.css' pour styler les templates HTML, deplus on utilise BOOTSTRAP aussi pour le style. Le site est divise en 15 fichier html, ou 4 sont des pages d'erreurs.

## account
```
## account_page.html

Contient le skeleton de la page du compte de l'utilisateur, l'utilisateur peut changer le password sur cette page

## dashboard.html

Contient le skeleton de la page dashboard pour l'admin, ou il peut voir tout les utilisateurs, les bloquer/débloquer et changer les roles

## my_books.html

Contient le skeleton de la page my books pour chaque utilisateur, la page contient tous les livres de l'utilisateur actuel. Il peut changer le status du livre (sold/available) et changer le prix du livre
```

## authentication
```
## create.html

Contient le skeleton de la page de creation de compte

## login.html

Contient le skeleton de la page login, pour rentrer dans la librairie

```

## book
```
## books.html

Contient le skeleton de la database de la librairie 

## delete_book.html

Contient le skeleton de la function d'effacer, avec une entree text pour le nom du livre à effacer

## edit_book.html

Contient le skeleton pour la fonction edit, avec une entree text pour le nom du livre à editer et les entrees pour le nouveu livre

## new_book.html

Contient le skeleton de la fonction add, avec les entrees text pour le nouveau livre
```

## errors
```
## 400.html

Contient le skeleton pour la page d'erreur: 400 Error -- Bad Request page

## 401.html

Contient le skeleton pour la page d'erreur: 401 Error -- Unauthorized

## 404.html

Contient le skeleton pour la page d'erreur: 404 Error -- Not Found

## 422.html

Contient le skeleton pour la page d'erreur: 422 Error -- Unprocessable Entity
```



```

## empty_page.html

Contient le skeleton HTML du site

## home.html

Contient le skeleton HTML de la page d'acceuil 

## my_macro.html

Contient le macro pour 'show_book(name, id, author, editor, price, owner-email, status)', 'show_book_count(count)', 'show_user(email, name, firstname, role, access)', 'show_book_home(name, id, author, editor, price, owner_email, users)', 'show_my_book(name, id, author, editor, price, status, active_user)' pour montrer les valeurs des livres dans la database et le nombre de livres dans la database, ainsi que les utilisateurs. Les pages my_books.html et home.html on une macro pour faciliter de montrer les données de la database avec des contraintes plus spécifique.
```

# Schema
Le repertoire schema contient les fichiers book.py et user.py, qui définissent les livres et les utilisateurs, par exemple ils définissent que l'utilisateur a un nom, prénom...

Dans le fichier book.py on a la classe BookSchema qui définit les livres et la classe CheckBook, qui controle que certaines données ne sont pas que des espaces vides.

# SQL Models
Le repertoire sql_models contient les fichiers books.py et users.py qui définissent comment les livres et les utilisateurs sont définies dans la database en SQLite.

# Autres fichiers

## app.py
Ce fichier est responsable pour réagir en cas d'erreurs HTTP et de définir au programme ou les services, routes, templates... sont dans les repertoires.

## database.py
Ce fichier est responable pour créer l'engine afin de créer la database et de pouvoir l'acceder.

## login.py
Ce fichier est responsable pour lancer le LoginManager afin de savoir quel utilisateur est login.

## main.py
Ce fichier est responsable que pour le lancement du server.

# Description

## First Iteration

Le programme nous donne la possibilite d'acceder aux livres de la librairie ('/all'), de compter le nombres des livres dans la librairie ('/count'). On peut aussi ajouter des livres ('/add'), effacer des livres ('/delete/book_name') et d'editer des livres ('/edit/book_name')

Le programme nous returne des erreurs HTTP si les parametres sont faux ou pose de problemes. Par exemple si on veut effacer ou editer un livre qui n'est pas dans la librairie.

## Second Iteration

Cette version du programme est une nouvelle iteration du TP1, toutes les fonctionalitees sont reprises, mais legerement modifier. La partie principale de cette iteration sont les templates HTML, pour avoir une interface HTML pour voir, ajouter, effacer,.., les livres au lieu d'avoir que du JSON. On a des buttons pour interagir avec les pages et des pages d'erreurs en cas d'erreurs.

## Third Iteration

Cette version du programme implemente des utilisateur, le but est d'avoir un ou plusieurs administrateurs qui peuvent ajouter, supprimer et editer des livres, et des client qui peuvent voir les livres qui sont dans la librarie. Les administrateurs peuvent aussi bloquer/debloquer des utilisateur et les promouvoir ou limoger. Chaque utilisateur a des informations personnelles tels que l'email, mot de passe nom et prenom, mais le programme leur donne aussi automatiquement un role et un access à la librarie. Chaque utilisateur peut changer leurs mot de passe dans la page account. Les pages d'erreurs montrent les erreurs avec un petit message adapte pour que les utilisateurs sachent ce qu'ils on fait de faut. 


## Fourth Iteration

Dans cette version du programme on implemente une database avec _SQLite_, pour faire cela quelques changement ont du été fait au fonctionalitées des iteration précédentes, afin d'accéder et changer les données de la database. De plus les livres on un prix, un status (sold/available) et un propriétaire (dont l'email est stocké avec le livre).

Chaque utilisateur a ces propres livres et peut changer le prix et le status du livre dans la page _My Books_, seul les administrateurs peuvent additioner, editer et supprimer par complet les livres. 

Chaque utilisateur peut acceder leurs informations de compte dans la page _Account_ et même changer quelques données. Ils peuvent changer leurs mot de passe on donnant le mot de passe actuel, et changer l'email, le nom et le prénom.

Sur la page _Home_ tous le monde peut voir les livres qui n'ont pas encore été vendus, sans se connecter. Après s'avoir connecté les utilisateurs ne verront que les livres qui n'ont pas le status de vendu.


