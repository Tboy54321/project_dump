from fastapi import status, HTTPException, Depends, APIRouter
from typing import List
import models, schemas, oauth2
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


@router.get('/categories', status_code=status.HTTP_200_OK, response_model=List[schemas.ExpenseCategory])
def get_categories(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    categories = db.query(models.ExpenseCategory).all()
    return categories

@router.get("/category/{id}")
def get_category(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    category = db.query(models.ExpenseCategory).filter(models.ExpenseCategory.id == id).first()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Expense with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return category


@router.post("/createcategory/", status_code=status.HTTP_201_CREATED)
def new_category(categories: schemas.ExpenseCategory, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # post_query = db.query(models.Posts).filter(models.Posts.id == id)
    print(current_user.email)
    new_categories = models.ExpenseCategory(**categories.dict())
    db.add(new_categories)
    db.commit()
    db.refresh(new_categories)
    return {'data': new_categories}

@router.put("/updatecategory/{id}", status_code=status.HTTP_201_CREATED)
def update_category(id: int, updated_category: schemas.ExpenseCategory, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    old_category = db.query(models.ExpenseCategory).filter(models.ExpenseCategory.id == id)
    expense = old_category.first()

    if expense == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    old_category.update(updated_category.dict(), synchronize_session=False)
    db.commit()
    return {"Updated post": old_category.first()}
    

@router.delete('/deletecategroy/{id}')
def delete_category(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    delete_query = db.query(models.ExpenseCategory).filter(models.ExpenseCategory.id == id)
    delete_query.delete(synchronize_session=False)
    db.commit()
    return (delete_query)
    # for post in my_posts:
    #     post = find_post(id)
    #     deleted_posts = my_posts.remove(post)
    #     if not id:
    #         raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail={f'post with {id} does not exist'})
    # return {"remaining posts" : my_posts}
