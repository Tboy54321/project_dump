from fastapi import status, HTTPException, Depends, APIRouter
from typing import List
import models, schemas, oauth2
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get('/getallposts', status_code=status.HTTP_200_OK, response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Posts).all()
    # posts = db.query(models.Posts).filter(models.Posts.user_id == current_user.id).all()
    return posts

@router.get("/getpost/{id}")
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    # post = db.query(models.Posts).filter(models.Posts.id == id).filter(models.Posts.user_id == current_user.id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    
    return post


@router.post("/createposts/", status_code=status.HTTP_201_CREATED)
def new_post(post: schemas.Post, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # post_query = db.query(models.Posts).filter(models.Posts.id == id)
    # print(current_user.email)
    new_post = models.Posts(user_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {'data': new_post}

@router.put("/updatepost/{id}", status_code=status.HTTP_201_CREATED)
def update_post(id: int, updated_post: schemas.Post, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    old_post = db.query(models.Posts).filter(models.Posts.id == id)
    post = old_post.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    old_post.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {"Updated post": old_post.first()}
    

@router.delete('/deletepost/{id}')
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    delete_query = db.query(models.Posts).filter(models.Posts.id == id)
    delete_post = delete_query.first()

    if delete_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    

    delete_query.delete(synchronize_session=False)
    db.commit()
    return (delete_query)
    # for post in my_posts:
    #     post = find_post(id)
    #     deleted_posts = my_posts.remove(post)
    #     if not id:
    #         raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail={f'post with {id} does not exist'})
    # return {"remaining posts" : my_posts}
