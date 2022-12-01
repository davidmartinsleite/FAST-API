# aqui temos as declarações dos nossos endpoints

from fastapi import APIRouter

from controle import controle_papeis as papeis
from controle import controle_cotacoes as cotacoes

rota = APIRouter()

rota.include_router(papeis.rota, prefix='/papeis', tags=['Papeis'])  # dessa forma todos os endpoints vão começar com "/papeis"

rota.include_router(cotacoes.rota, prefix='/cotacoes', tags=['Cotaçôes'])
