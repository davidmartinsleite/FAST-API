import os
from datetime import datetime, timedelta
from typing import Union, Any

from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
# o "sha256_crypt" é um algoritimo de cripto grafia

# vamos criar o token JWT, ele é bem utilizado
# vamos criar uma chave para ele acinar o token, ele vai gerar um hash do token e
# colocar no final token, garantindo que o mesmo não foi alterado
SECRET_KEY = os.getenv('SECRET_KEY', 'vcufmv')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS512')  # esse é o algoritimo que vamos usar no token
ACCESS_TOKEN_EXPIRE_HOURS = 24


# aqui ele vai criar o token
def criar_token_jwt(subject: Union[str, Any]) -> str:
    # aqui ele vai pegar o horario atual e somar com 24 horas
    expire = datetime.utcnow() + timedelta(
        hours=ACCESS_TOKEN_EXPIRE_HOURS
    )
    # "sub" é o sujeito q estamos colocando no token, vamos colocar o ID do usuio aqui,
    # então vamos ter uma data de expiração e um id de usuario
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS512")
    return encoded_jwt


# pega a senha que acabou de ser digitada, e comparar com o hash q está no usuario dela
# para verificar se os 2 tem o mesmo valor
def verificar_senha(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# obtem o hash apartir de uma senha
def pegar_senha_hash(password: str) -> str:
    return pwd_context.hash(password)
