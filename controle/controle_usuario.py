from typing import List
from fastapi import APIRouter
from controle.uteis.deletar_controle import deletar_controle
from modelos.respostas.resposta_do_usuario import RequerimentoUsuario
from modelos.solicitacoes.atualizar_usuario import AtualizarRequerimentoUsuario
from modelos.solicitacoes.criar_usuario import CriarSolicitacaoUsuario

# from models.requests.usuario_update import UsuarioUpdateRequest
# from models.requests.usuario_create import UserCreateRequest
# from models.responses.usuario_response import UsuarioResponse

from modelos.usuario import Usuario

from controle.uteis.modificar_controle import modificar_controle
from controle.uteis.pegar_controle import pegar_controle
from controle.uteis.pegar_tudo_controle import pegar_tudo_controle

rota = APIRouter()


# criar um usuario é um pouco diferente

# essa função RequerimentoUsuario ele retorna ao endpoint apenas os elementos que sejam
# necessarios para visualização, evitando mostrar o password hash, isso pode ser
# implementado em qualquer coisa que não queira mostrar o endpoint
@rota.post("/", response_model=RequerimentoUsuario)
# primerio vamos criar uma requisição de criação de usuario
async def add_item(create_request: CriarSolicitacaoUsuario):
    # vamos pegar os atributos que vamos receber da requisição e transformalos em um dict
    atributos = create_request.dict(exclude_unset=True)
    # vamos criar um usuario e colocar o dict no usuario para ser atribuido
    usuario = Usuario(**atributos)
    return await usuario.save()  # vai retornar e salvar os valores salvos


# isso é uma lista desse tipo de resposta, então ele vai pegar varios usuarios e
# transformar pra esse formato
@rota.get("/", response_model=List[RequerimentoUsuario])
@pegar_tudo_controle(Usuario)
async def list_item():
    pass


@rota.get("/{id}", response_model=RequerimentoUsuario)
@pegar_controle(Usuario)
async def get_papel(id: int):
    pass


@rota.patch("/{id}", response_model=RequerimentoUsuario)
@modificar_controle(Usuario)
# aqui ele usar a "AtualizarRequerimentoUsuario" para modificar ALGUM elemento caso a senha seja igual
async def patch_papel(propriedades_atualizacao: AtualizarRequerimentoUsuario, id: int):
    pass


@rota.delete("/{id}")
@deletar_controle(Usuario)
async def delete_papel(id: int):
    pass
