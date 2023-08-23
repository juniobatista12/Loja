from pydantic import BaseModel

class LoginModel(BaseModel):
    email: str
    senha: str

class CadastroModel(BaseModel):
    cpf: str
    email: str
    senha: str