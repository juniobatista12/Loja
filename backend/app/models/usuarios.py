from pydantic import BaseModel

class LoginModel(BaseModel):
    email: str
    senha: str