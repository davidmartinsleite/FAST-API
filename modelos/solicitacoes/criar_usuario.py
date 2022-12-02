from pydantic import BaseModel, Field, validator
from seguranca import pegar_senha_hash


class CriarSolicitacaoUsuario(BaseModel):
    nome: str
    email: str
    hash_password: str = Field(alias='password')  # isso é apenas para criar um apelido

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):  # ele vai pegar o senha e gerar um hash dela
        return pegar_senha_hash(v)
