from typing import Optional, Union  # isso serve para dizer que algo não é obrigatorio, mesma coisa que "optional"

from fastapi import FastAPI, Header, Response, Cookie

from pydantic import BaseModel  # essa lib serve para pegar dados contidos no corpo de uma requisição


class Item(BaseModel):  # essa classe erda de "BaseModel"
    id: int
    descricao: str
    valor: float


app = FastAPI()  # nome da aplicação você pode mudar para qualquer nome, lembre de mudar na execução da aplicação: uvicorn main:aplicativo --reload


@app.get("/")  # get é um metodo http, você pode mudar para 'post' ou 'delete'
def read_root(usuario: Union[str, None] = Header(None)):  # ele vai criar titulo
    return {"user-agente": usuario}
# o "Header" pode retornar por padrão um "none" ou vc pode mudar esse retorno para uma msg
# caso vc use "user_agent" como saida ele vai retornar os dados do seu navegador !!!
# def read_root(user_agent: Union[str, None] = Header(None)):


@app.get("/cookie")  # quando queremos quardar alguma preferencia do usuario
def cookie(response: Response):  # vamos usar o "Response" para
    response.set_cookie(key="meucookie", value="123456")  # ele retorna uma chave e valor, esse valor pode ser a chave da sessão
    return {'cookie adicionado': True}


@app.get('/pegar-Cookie')
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {'Cookie coletado': meucookie}
# ele vai pegar o Cookie que esteja salvo no navegador


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/item")  # esse é o caminho para o endpoint
def adicionar_item(novo_item: Item, outro_item: Item):  # aqui vamos colocar como parametro a classe "Item"
    # tambem podemos adicionar mais de um conjunto como o "outro_item" que tambem recebe o "Item"
    return [novo_item, outro_item]  # retornamos o resultado de "Item", ou os resultados


# para iniciar o programa: uvicorn main:app --reload
# o "--reload" serve para dar auto reload serve para qualquer auteração do codigo ele recarrega automaticamente
# se você mudar o arquivo de "main" para outro é só mudar na execução: uvicorn principal:app --reload
# para acessor o swagger do enderesso basta um /docs: http://127.0.0.1:8000/docs
