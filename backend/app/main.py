from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.controllers.usuarios as UsuariosAPI

app = FastAPI()

# Configurar as origens permitidas
origins = [
    "http://localhost:3000",  # URL do frontend
    # Adicione outras origens permitidas
]

# Adicionar o middleware CORS ao aplicativo
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UsuariosAPI.router)