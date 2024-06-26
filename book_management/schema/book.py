from pydantic import BaseModel, Field, ValidationError

class BookSchema(BaseModel):
    name: str = Field(min_length = 1)
    id: str = Field(min_length = 1)
    author: str = Field(min_length = 1)
    editor: str 
    price: str = Field(min_length = 1)
    owner_email: str = Field(min_length=1)
    status: str = Field(min_length=1)

class CheckBook():
    def check_book(book):
        if(book['name'].isspace() or book['author'].isspace() or book['id'].isspace()):
            return None
        return True
    

    
    