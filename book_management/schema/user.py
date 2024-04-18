from pydantic import BaseModel

class UserSchema(BaseModel):
    email:str
    name: str
    firstname: str
    password: str
    role: str
    access: bool