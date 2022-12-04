import ormar
import re
from pydantic import validator
import pydantic

from config import database, metadata

funcoes_validas = ["admin", "operador", "investidor"]  # aqui são as funções do sistema


class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100, unique=True)  # torna o email unico, pq vamos usar para fazer o login posteriormente
    hash_password: str = ormar.String(max_length=255)
    funcoes: pydantic.Json = ormar.JSON(default=[])  # essa propriedade constroi uma vetor json vazio ou preenchido, aqui poderia ser um relacionamento

# validadores
    @validator('email')
    def valida_formatacao_sigla(cls, v):
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(v):  # valida se o email tem as principais caracteristicas de um email
            raise ValueError('O formato do email é inválido!')
        return v

    @validator('funcoes')
    def valida_funcao_existem(cls, v):
        # vamos pegar o valor que está em "funcoes" e ver se ele é uma lista
        if not isinstance(v, list):
            # se não for uma lista ele retorna uma semagem de erro tipo "ValueError"
            raise ValueError(f'As funções de um usuário deve ser uma lista!')
        for funcao in v:  # se for uma lista
            if not isinstance(funcao, str) or funcao not in funcoes_validas:
                raise ValueError(f'A função {funcao} não é um função válida!')
        return v

    @validator('funcoes')
    def remove_funcoes_duplicadas(cls, v):  # esse validade remove listas duplicadas
        return list(set(v))  # ele transforma em um "set" que n pode ter um valor duplicado, depois ele transforma novamente em uma lista
