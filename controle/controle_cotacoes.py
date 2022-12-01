from fastapi import APIRouter

from controle.uteis.adicionar_controle import adicionar_controle
from controle.uteis.deletar_controle import deletar_controle
from controle.uteis.entidade_nao_encontrada import entidade_nao_encontrada
from controle.uteis.pegar_controle import pegar_controle
from controle.uteis.pegar_tudo_controle import pegar_tudo_controle
from modelos.cotacao import Cotacao

rota = APIRouter()

@rota.post("/")
@adicionar_controle
async def adicionar_cotacoes(entidade: Cotacao):
    pass

@rota.get("/")
@pegar_tudo_controle(Cotacao)
async def pegar_todas_cotacoes():
    pass

@rota.get("/{id}")
@pegar_controle(Cotacao, [Cotacao.papel])
async def pegar_cotacao(id: int):
    pass



@rota.delete("/{id}")
@deletar_controle(Cotacao)
async def deletar_cotacao(id: int):
    pass

