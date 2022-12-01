from typing import Optional

import ormar
from datetime import datetime
from config import database, metadata
from modelos.papel import Papel


class Cotacao(ormar.Model):  # essa classe vai erdar de ormar.model
    class Meta:
        metadata = metadata
        database = database
        tablename = 'cotacoes'

    id: int = ormar.Integer(primary_key=True)
    valor: float = ormar.Float(minimum=0)  # se o valor for menor que zero ele vai dar erro
    horario: datetime = ormar.DateTime(timezone=False)
    # agora vamos criar um relacionamentos um-para-muitos
    papel: Optional[Papel] = ormar.ForeignKey(  # essa propriedade é do tipo chave estrangeira
        Papel,
        skip_reverse=True
    )
