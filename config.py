# esse arquivo vai armazenar todas as depedencias
import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
# esse database vai ficar armazenado as configurações com o banco de dados
# "getenv()" pode criar variaveis de ambientes no "OS"
# ele vai procurar "DATABASE_URL" caso n tenha ele vai pegar a "sqlite:///db.sqlite"
# o "sqlite" funciona com um arquivo, ele vai criar um arquivo "db.sqlite"
# isso pode ser auterado para MYsql ou Postgre

# teste automatizado
TESTE_DATABASE = os.getenv('TESTE_DATABASE', 'false') in ('true', 'yes')
# isso vai criar a variavel de teste, caso queira fazer o teste setar o 'false' para 'true'
# ele vai fazer com que os dados não sejam usado, fazendo testes com o bando de dados limpo
database = databases.Database(DATABASE_URL, force_rollback=TESTE_DATABASE)
# aqui estamos criando o bando de dados falso para o teste
# ele não vai gravar os dados no arquivo de verdade que estão sendo gerados pela API !
metadata = sqlalchemy.MetaData()
