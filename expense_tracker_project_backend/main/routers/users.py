from fastapi import status, HTTPException, Depends, APIRouter
import models, schemas, utils
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/users",
    tags=["Signing In new users"]
)


# ENDPOINT TO REGISTER NEW USERS
@router.post('/signup', status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Endpoint to register new users"""
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.dict())
    try:
        db.add(new_user)
        # print(new_user.email)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    return new_user


# ENDPOINT TO GETTING A USER BASED ON EMAIL
@router.get('/getuser/{email}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.UserOut)
def get_user(email: str, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {email} does not exist")
    return user

# ENDPOINT TO GETTING ALL USERS
@router.get('/getallusers', status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return users
