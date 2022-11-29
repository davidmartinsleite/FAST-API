from fastapi import APIRouter
from modelos.papel import Papel


rota = APIRouter()  # isso cria uma rota para a criação do @app que já foi criado no main

banco_de_dados = []


@rota.post('/')
def adicionar_papel(item: Papel):
    banco_de_dados.append(item)
    return item


@rota.get('/')
def listar_papeis():
    return banco_de_dados
