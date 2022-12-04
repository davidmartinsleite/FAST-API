from typing import List
from fastapi import APIRouter, Form, HTTPException, Depends
from controle.dependencias.usuario import pegar_usuario_logado, pegar_usuario_com_funcao
from controle.uteis.deletar_controle import deletar_controle
from controle.uteis.entidade_nao_encontrada import entidade_nao_encontrada
from controle.uteis.pegar_tudo_controle import pegar_tudo_controle
from controle.uteis.pegar_controle import pegar_controle
from controle.uteis.modificar_controle import modificar_controle

from modelos.solicitacoes.atualizar_usuario import AtualizarRequerimentoUsuario
from modelos.solicitacoes.criar_usuario import CriarSolicitacaoUsuario
from modelos.respostas.resposta_do_usuario import RequerimentoUsuario

from modelos.usuario import Usuario
from seguranca import verificar_senha, criar_token_jwt

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
async def get_papel(id: int,
                    usuario_logado: Usuario = Depends(pegar_usuario_logado)  # agora basta colocar essa função que habilita a ultilização de login para a função
                    ):
    pass


@rota.patch("/{id}", response_model=RequerimentoUsuario)
@modificar_controle(Usuario)
# aqui ele usar a "AtualizarRequerimentoUsuario" para modificar ALGUM elemento caso a senha seja igual
async def patch_papel(propriedades_atualizacao: AtualizarRequerimentoUsuario, id: int):
    pass


#agora é necessario fazer login para usar essa função
@rota.delete("/{id}")
@deletar_controle(Usuario)
async def delete_papel(
        id: int,
        usuario_logado: Usuario = Depends(pegar_usuario_com_funcao(funcoes=['admin']))):
    pass


@rota.post("/login")
# esse controller vai receber um usuario e uma senha
async def login(username: str = Form(...), password: str = Form(...)):
    # ele vai tentar procurar esse usuario pela base de dados
    user = await Usuario.objects.get_or_none(email=username)
    # agora ele vai verificar se o usuario e none ou não,
    # depois ele vai verificar a senha está certa, comparando com o hash
    if not user or not verificar_senha(password, user.hash_password):
        raise HTTPException(status_code=403,
                            detail="Email ou nome de usuário incorretos"
                           )
    # caso ache a usuario e senha ele vai gerar uma resposta que vai devolver o token e seu tipo
    return {
        "access_token": criar_token_jwt(user.id),
        "token_type": "bearer",
    }
# esse retorno de dados com o token vai gerar um numero como esse
# eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzAwODM4NDAsInN1YiI6IjEifQ.hfpIpsrnVe9i-JBl0UtfLb-zRLL8DDDwynb-L33LLb4em60lJmYyYk_JTbYvol5JPIhAtSw9YhrfLdppLYiXOA
# esse token possui os dados para validação de um usuario
# NOTA: CUIDADO COM OS DADOS COLOCADOS NO TOKEN, ELES PODEM SER ACESSADOS
# use o site: https://jwt.io/ para verificar os dados do token


# cria as funções
@rota.post("/{id}/funcoes/{funcao}", response_model=RequerimentoUsuario)
@entidade_nao_encontrada  # verifica se o usuario foi encontrado ou não
async def add_funcao_usuario(id: int, funcao: str):
    # o usuario vai pegar o ID
    usuario = await Usuario.objects.get(id=id)
    # vai adicionar a lista de funcao(isso tem q ser uma string)
    usuario.funcoes += [funcao]  # NOTA: isso é uma lista, más caso tente "usuario.funcoes.append(funcao)" vai dar erro!!!
    # vai fazer um update
    await usuario.update()
    # vai retornar o usuario
    return usuario


@rota.delete("/{id}/funcoes/{funcao}", response_model=RequerimentoUsuario)
@entidade_nao_encontrada
async def delete_funcao_usuario(id: int, funcao: str):
    usuario = await Usuario.objects.get(id=id)
    usuario.funcoes.remove(funcao)
    await usuario.update()
    return usuario
