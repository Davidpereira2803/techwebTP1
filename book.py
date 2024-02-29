def add_book(library, title, id, author, editor):

    book = {"titre" : title, "identifiant": id, "auteur" : author, "editeur" : editor} 
    library.append(book)

    print("Livre ajouté")


def modify_book_data(library, title, new_title, new_id, new_author, new_editor):

    for book in library: 

        if book["titre"] == title :

            book["titre"]= new_title
            book["identifiant"] = new_id
            book["auteur"] = new_author 
            book["editeur"] = new_editor 

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
            print(f"{i}. {book['titre']}, identifié par le code {book['identifiant']}, écrit par {book['auteur']}, aux éditions {book['editeur']}")

        print(f"Nombre total de livres : {len(library)}")