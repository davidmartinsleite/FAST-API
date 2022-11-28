from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    quantidade: int
    descricao: str
    valor: float


app = FastAPI()

banco_de_dados = []

@app.post('/item')  # insere elementos no banco de dados, ele faz apenas um append
def adicionar_item(item: Item):
    banco_de_dados.append(item)
    return item


@app.get('/item')  # criar um endpoint para verificar todos os objetos criados
def lista_item():
    return banco_de_dados


@app.get('/item/valor_total')
def pegar_valor_total():
    valor_total = 0.0
    # valor_total = sum([item.valor * item.quantidade for item in banco_de_dados])
    # OU
    for item in banco_de_dados:
        valor_total += (item.quantidade * item.valor)
    return {'valor_total': valor_total}




# uvicorn ex02:app --reload