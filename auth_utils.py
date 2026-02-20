# password utility file
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    if len(password) > 72:
        password = password[:72]
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str):
    if len(plain_password) > 72:
        plain_password = plain_password[:72]
    return pwd_context.verify(plain_password, hashed_password)
