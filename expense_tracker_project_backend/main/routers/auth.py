from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
import schemas, models, utils, database, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authenticatication'])


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    """ Endpoint to authenticate users and provide JWT tokens"""
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

# IMPLEMENTATION OF LOGOUT FUNCTION

@router.post("/logout")
def logout(token: str = Depends(oauth2.oauth2_scheme), db: Session = Depends(database.get_db)):
    blacklisted_token = models.TokenBlacklist(token=token)
    db.add(blacklisted_token)
    db.commit()
    return {"message": "Successfully logged out"}