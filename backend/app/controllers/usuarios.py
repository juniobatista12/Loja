import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.usuarios import LoginModel, CadastroModel
from app.db.usuarios import UsuarioDB

router = APIRouter(
    prefix="/Usuarios",
    tags=["Usuarios"],
    responses={404: {"description": "Não encontrado"}}
)

@router.post("/login")
def login(body: LoginModel):
    body = json.loads(body.json())
    where = [(item,body[item],'str') for item in body]
    conn = UsuarioDB()
    if conn.getUsuario(where):
        return JSONResponse(
            status_code=200,
            content={"messagem": "Usuario autenticado com sucesso"}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"messagem": "Falha na autenticação"}
        )
    
@router.post("/cadastrar")
def cadastrar(body: CadastroModel):
    body = json.loads(body.json())
    values = [(item,body[item],'str') for item in body]
    conn = UsuarioDB()
    if conn.putUsuario(values):
        return JSONResponse(
            status_code=200,
            content={"mensagem": "Usuário criado com sucesso"}
        )
    else:
        return JSONResponse(
            status_code=409,
            content={"mensagem": "Usuário já existe"}
        )