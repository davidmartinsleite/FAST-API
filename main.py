from typing import Union  # isso serve para dizer que algo não é obrigatorio, mesma coisa que "optional"

from fastapi import FastAPI

app = FastAPI()  # nome da aplicação você pode mudar para qualquer nome, lembre de mudar na execução da aplicação: uvicorn main:aplicativo --reload


@app.get("/")  # get é um metodo http, você pode mudar para 'post' ou 'delete'
def read_root():
    return {"Hello": "World 2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# para iniciar o programa: uvicorn main:app --reload
# o "--reload" serve para dar auto reload serve para qualquer auteração do codigo ele recarrega automaticamente
# se você mudar o arquivo de "main" para outro é só mudar na execução: uvicorn principal:app --reload
# para acessor o swagger do enderesso basta um /docs: http://127.0.0.1:8000/docs
