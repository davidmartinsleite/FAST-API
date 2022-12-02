from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
# o "sha256_crypt" é um algoritimo de cripto grafia

# pega a senha q acabou de ser digitada, e comparar com o hash q está no usuario dela
# para verificar se os 2 tem o mesmo valor
def verificar_senha(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# obtem o hash apartir de uma senha
def pegar_senha_hash(password: str) -> str:
    return pwd_context.hash(password)
