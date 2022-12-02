# isso vai servir para enviar dados ao endpoint, nesse caso vai evitar o uso do password no retorno

from pydantic import BaseModel


class RequerimentoUsuario(BaseModel):
    id: int
    nome: str
    email: str
