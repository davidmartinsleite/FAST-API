import ormar.exceptions
from fastapi import APIRouter, Response
from modelos.papel import Papel



rota = APIRouter()  # isso cria uma rota para a criação do @app que já foi criado no main



# NOTA: esse banco de dados e feito de forma assincrona então vamos adiconar o "async"
@rota.post('/')
async def adicionar_papel(papel: Papel):
    await papel.save()
    # o ORM vai ser assincrono, então preciso que ele espere a operação do ORM
    # terminar e que ele me retorne o resultado para continuar nessa função
    return papel


@rota.get('/')
async def listar_papeis():
    return await Papel.objects.all()

@rota.get('/{papel_id}')
async def get_papel(pael_id: int, response: Response):
    try:
        papel = await Papel.objects.get(id=pael_id)
        return papel
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'mesagem': 'entidade não encontrada'}
