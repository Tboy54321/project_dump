from fastapi import status, HTTPException, Depends, APIRouter
from typing import List
import models, schemas, oauth2
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get('/budgets', status_code=status.HTTP_200_OK, response_model=List[schemas.BudgetOut])
def get_budgets(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # budgets = db.query(models.Budget).all()
    budgets = db.query(models.Budget).filter(models.Budget.user_id == current_user.id).all()
    # print(budgets)
    return budgets

@router.get("/budget/{id}", status_code=status.HTTP_200_OK)
def get_budget(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # budget = db.query(models.Budget).filter(models.Budget.id == id).first()
    budget = db.query(models.Budget).filter(models.Budget.id == id).filter(models.Budget.user_id == current_user.id).first()

    if not budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Budget with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    
    if budget.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
        
    return budget


@router.post("/createbudget/", status_code=status.HTTP_201_CREATED)
def new_budget(budgets: schemas.BudgetIn, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # post_query = db.query(models.Posts).filter(models.Posts.id == id)
    print(current_user.email)
    new_budgets = models.Budget(user_id=current_user.id, **budgets.dict())
    db.add(new_budgets)
    db.commit()
    db.refresh(new_budgets)
    return {'data': new_budgets}

@router.put("/updatebudget/{id}", status_code=status.HTTP_201_CREATED)
def update_budget(id: int, updated_budget: schemas.BudgetIn, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    old_budget = db.query(models.Budget).filter(models.Budget.id == id)
    budget = old_budget.first()

    if budget == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Budget with id: {id} was not found")
    
    if budget.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    old_budget.update(updated_budget.dict(), synchronize_session=False)
    db.commit()
    return {"Updated post": old_budget.first()}
    

@router.delete('/deletebudget/{id}')
def delete_budget(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    delete_query = db.query(models.Budget).filter(models.Budget.id == id)
    deleted_budget = delete_query.first()

    if not deleted_budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Budget with id: {id} was not found")
    
    if deleted_budget.user_id != current_user.id:
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
