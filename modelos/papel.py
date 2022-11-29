import ormar
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
