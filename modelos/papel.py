import ormar
import re  # essa lib cria expreções regulares
from pydantic import validator
from config import database, metadata


class Papel(ormar.Model):
    class Meta:  # ele cria uma classe dentro da outra pra poder se conectar com o banco
        metadata = metadata
        database = database
        tablename = 'papeis'

    id: int = ormar.Integer(primary_key=True)  # vai ser o PK e auto incrementado
    nome: str = ormar.String(max_length=100)
    sigla: str = ormar.String(max_length=10)
    cnpj: str = ormar.String(max_length=20)

    @validator('sigla')
    def valida_formatacao_sigla(cls, v):
        if not re.compile('^[A-Z]{4}[0-9]{1,2}$').match(v):  # o "match() é para comparar os resultados
        # "^" que o teste comece desde a primeira letra, [A-Z] apenas letras maiusculas,
        # {4} repetir 4 vrezes, [0-9] numeros entre 0 e 9 e {1,2} que tenha de 1 ou 2 numeros,
        # $ quero que a string acabe aqui.
            raise ValueError('A seigla do papel é invalida!')
        return v
