import ormar
from functools import wraps

from ormar.models import model

from controle.uteis.entidade_nao_encontrada import entidade_nao_encontrada


def pegar_tudo_controle(modelo: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper():
                return await modelo.objects.all()
        return wrapper
    return inner
