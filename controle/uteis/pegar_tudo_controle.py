import ormar
from functools import wraps


def pegar_tudo_controle(modelo: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper():
                return await modelo.objects.all()
        return wrapper
    return inner
