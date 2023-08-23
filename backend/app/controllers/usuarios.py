import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.usuarios import LoginModel
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