from fastapi import status, HTTPException, Depends, APIRouter, BackgroundTasks
from typing import List
import models, schemas, oauth2, calculateExpensePercentage
from datetime import datetime

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
    if budgets.end_date < budgets.start_date:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="End date cannot be earlier than start date")
    
    overlap_budget = db.query(models.Budget).filter(
        models.Budget.user_id == current_user.id,
        models.Budget.category == budgets.category,
        models.Budget.start_date >= budgets.start_date,
        models.Budget.end_date <= budgets.end_date
        ).first()
    

    if overlap_budget:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Budget of this category already exists within this period")
    
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


# @router.post("/check-budget-status/{user_id}")
# def check_budget_status(user_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     if user_id != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")

#     background_tasks.add_task(crud.check_budget_status, user_id, db)
#     return {"message": "Budget check scheduled"}

# @router.get("/notifications", response_model=List[schemas.NotificationOut])
# def get_notifications(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     notifications = db.query(models.Notification).filter(models.Notification.user_id == current_user.id).all()
#     return notifications

@router.get("/notifications", response_model=List[schemas.NotificationOut])
def get_notifications(background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    background_tasks.add_task(calculateExpensePercentage.check_budget_status, current_user.id, db)
    notifications = db.query(models.Notification).filter(models.Notification.user_id == current_user.id).all()
    return notifications

@router.delete('/delete-notification/{id}')
def delete_notifications(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    delete_query = db.query(models.Notification).filter(models.Notification.id == id)
    deleted_notification = delete_query.first()

    if not deleted_notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Notification with id: {id} was not found")
    
    if deleted_notification.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    delete_query.delete(synchronize_session=False)
    db.commit()
    return (delete_query)