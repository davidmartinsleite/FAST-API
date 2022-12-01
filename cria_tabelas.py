# esse script vai criar o modelo databela que vamos precisar
import sqlalchemy
from config import DATABASE_URL, metadata
import modelos.importacoes_de_modelos

def configurar_banco(database_url = DATABASE_URL):
    # essa função vai criar as tabelas no banco, so vamos criar um parametro
    print(database_url)
    engine = sqlalchemy.create_engine(database_url)
    # vamos criar uma engine para se conectar com o banco
    metadata.drop_all(engine)
    metadata.create_all(engine)


if __name__ == '__main__':
    configurar_banco()

# quando chamar o script direto do terminal
# ele vai criar todas as colunas nop banco "papeis"