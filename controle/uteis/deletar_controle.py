from functools import wraps
import ormar
from controle.uteis.entidade_nao_encontrada import entidade_nao_encontrada

# esse modelo vai ser passado para a definição que é o ormal.model
# ele vai ser passado para dentro para o outro decorator
def deletar_controle(modelo: ormar.Model):
    # esse decorator via receber a função de fora, ele só vai serveir para captar a função de fora
    def inner(func):
        @entidade_nao_encontrada  # ele vai encapsular esse dado recebido do .get logo acima e fazer um tratamento
        # NOTA: nós tiramos essa parte do "controle_papeis" e encapsulamos tudo de uma só vez
        @wraps(func)
        # a função do controle é assincrona, aqui vamos colocar tudo para termos genericos
        async def wrapper(id: int):
            entidade = await modelo.objects.get(id=id)  # aqui ele vai receber o objeto com seus elementos
            return await entidade.delete()  # e aqui ele vai deletar esses elementos
        return wrapper  # aqui só retorna a função
    return inner  # aqui tambem
