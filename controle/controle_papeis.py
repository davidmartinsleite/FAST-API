import ormar.exceptions
from fastapi import APIRouter, Response
from modelos.papel import Papel
from modelos.solicitacoes.atualiza_papel import AtualizarPapel

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

@rota.patch('/{papel_id}')
async def patch_papel(propriedades_atualizacao: AtualizarPapel, papel_id: int, response: Response):
    try:
        papel_salvo = await Papel.objects.get(id=papel_id)
        propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
        await papel_salvo.update(**propriedades_atualizadas)
        return papel_salvo
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {'mensagem': 'Entidade não encontrada'}
