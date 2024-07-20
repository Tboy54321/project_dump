from jose import JWTError, jwt
from datetime import timedelta, datetime
import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "7et943-t0es[jew9r3-43[r821909y[llhruetwq8r430tkrehewue62093-oi4oyr289803254o3r89qiwpwtmnrekdy]]"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception, db: Session):

    try:
        # HANDLING FOR LOGOUT FUNCTION (blacklisted_token)
        # blacklisted_token = db.query(models.TokenBlacklist).filter(models.TokenBlacklist.token).first()
        blacklisted_token = db.query(models.TokenBlacklist).filter(models.TokenBlacklist.token == token).first()

        if blacklisted_token:
            raise credentials_exception
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print(payload)

        id: int = payload.get("user_id")

        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=id)
        # print(token_data)
    except JWTError as J:
        print(J)
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception  = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Berarer"})

    token = verify_access_token(token, credentials_exception, db)
    user = db.query(models.Users).filter(models.Users.id == token.id).first()
    if not user:
        raise credentials_exception
    print(user.id)

    return user