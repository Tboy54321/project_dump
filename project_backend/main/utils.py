from passlib.context import CryptContext
from passlib.exc import UnknownHashError
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(real_password, hashed_password):
    try:
        return pwd_context.verify(real_password, hashed_password)
    except UnknownHashError as e:
        print (e)