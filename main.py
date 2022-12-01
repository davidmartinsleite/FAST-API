from fastapi import FastAPI
from rotas import rota


app = FastAPI()

@rota.get('/')
async def pegar_rota():
    return {'mensagem': 'api de papeis'}


app.include_router(rota, prefix='')

# uvicorn main:app --reload


# para baixar os arquivos das libs em um .txt basta:
# "pip freeze" mostra as libs instaladas na maquina
# "pip freeze > nome_do_arquivo.txr" salva os nomes com as versões em um .txt
# "pip install -r nome_do_arquivo.txt" baixa os arquivos para a maquina
