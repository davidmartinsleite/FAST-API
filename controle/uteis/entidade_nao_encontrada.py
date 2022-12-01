from fastapi import HTTPException
import ormar
from functools import wraps

# essa função vai encapsular outra função
def entidade_nao_encontrada(func):  # aqui vemos q ela vai criar uma função como parametro
    @wraps(func)  # esse "wraps" vai pegar os dados que estão sendo recebidos como parametros, e atribuir para a função interna func
    async def inner(*args, **kwargs):  # "inner" é para receber uma função interna, esses parametros são genericos, não sabemos oq vamos receber
        try:
            return await func(*args, **kwargs)
        except ormar.exceptions.NoMatch:  # aqui ele vai pegar a exeção do ormar
            raise HTTPException(status_code=404, detail='Entidade não encontrada')
            # "HTTPException" é um erro do proprio fastapi, com ele podemos passar o codigo que queremos q ele retorne, ele vai enviar uma mensagem caso ocorra o erro
    return inner  # aqui retornamos a função que foi criada
