def add_book(library, title, author, year):

    book = {"titre":title, "auteur":author, "annee":year} 
    library.append(book)

    print("Livre ajouté")


def modify_book_data(library, title, new_title, new_author, new_year):

    for book in library: 

        if book["titre"] == title :

            book["titre"]= new_title
            book["auteur"] = new_author 
            book["annee"] = new_year 

            print("Livre modifié")


def delete_book(library, title):
     
    for book in library: 
         
        if book in library:
             
            library.remove(book)

            print("Livre supprimé")
            return 
         
    print(f"Livre non trouvé")


def display_list(library):

    if not library:
        
        print("La bibliothèque est vide.")

    else:

        print("Liste des livres :")

        for i, book in enumerate(library, start = 1):
            print(f"{i}. {book['titre']} par {book['auteur']}, paru en {book['annee']}")

        print(f"Nombre total de livres : {len(library)}")