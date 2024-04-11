from pydantic import BaseModel, Field, ValidationError

class Book(BaseModel):
    name: str = Field(min_length = 1)
    id: str
    author: str = Field(min_length = 1)
    editor: str = Field(min_length = 1)

class CheckBook():
    def check_book(book):
        if(book['name'].isspace() or book['author'].isspace() or book['editor'].isspace()):
            return None
        return True
    

    
    