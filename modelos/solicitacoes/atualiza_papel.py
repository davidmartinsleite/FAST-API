from typing import List, Optional
from pydantic import BaseModel


class AtualizarPapel(BaseModel):
    nome: Optional[str] = None
    cnpj: Optional[str] = None
