from typing import Optional
from pydantic import BaseModel, Field, validator
from seguranca import pegar_senha_hash


class AtualizarRequerimentoUsuario(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    hash_password: Optional[str] = Field(alias='password', default=None)

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        if v:
            return pegar_senha_hash(v)
        return v
