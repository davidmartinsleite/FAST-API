from fastapi import APIRouter

from controle import controle_papeis as papeis

rota = APIRouter()

rota.include_router(papeis.rota, prefix='/papeis')  # dessa forma todos os endpoints vão começar com "/papeis"
