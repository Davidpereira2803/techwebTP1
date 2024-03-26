from pydantic import BaseModel

class User(BaseModel):
    email:str
    name: str
    firstname: str
    password: str
    role: str
    access: bool