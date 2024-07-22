from fastapi import status, HTTPException, Depends, APIRouter, BackgroundTasks
from typing import List
import models, schemas, oauth2, calculateExpensePercentage
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


def check_budget_status(user_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    background_tasks.add_task(calculateExpensePercentage.check_budget_status, user_id, db)
    notifications = db.query(models.Notification).filter(models.Notification.user_id == current_user.id).all()
    return notifications


@router.get('/expenses', status_code=status.HTTP_200_OK, response_model=List[schemas.ExpenseOut])
def get_expenses(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # budgets = db.query(models.Budget).all()
    expenses = db.query(models.Expense).filter(models.Expense.user_id == current_user.id).all()
    # print(budgets)
    return expenses

@router.get("/expense/{id}", status_code=status.HTTP_200_OK)
def get_expense(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # budget = db.query(models.Budget).filter(models.Budget.id == id).first()
    expense = db.query(models.Expense).filter(models.Expense.id == id).filter(models.Expense.user_id == current_user.id).first()

    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Expense with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    
    if expense.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
        
    return expense


@router.post("/createxpense/", status_code=status.HTTP_201_CREATED)
def new_expense(expenses: schemas.ExpenseIn, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), background_tasks = BackgroundTasks):
    # post_query = db.query(models.Posts).filter(models.Posts.id == id)
    print(current_user.email)
    new_expenses = models.Expense(user_id=current_user.id, **expenses.dict())
    db.add(new_expenses)
    db.commit()
    db.refresh(new_expenses)
    return {'data': new_expenses}

@router.put("/updatexpense/{id}", status_code=status.HTTP_201_CREATED)
def update_expense(id: int, updated_expense: schemas.ExpenseIn, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    old_expense = db.query(models.Expense).filter(models.Expense.id == id)
    expense = old_expense.first()

    if expense == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Expense with id: {id} was not found")
    
    if expense.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    
    old_expense.update(updated_expense.dict(), synchronize_session=False)
    db.commit()
    return {"Updated expense": old_expense.first()}
    

@router.delete('/deletexpense/{id}')
def delete_expense(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    delete_query = db.query(models.Expense).filter(models.Expense.id == id)
    deleted_expense = delete_query.first()

    if not deleted_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Expense with id: {id} was not found")
    

    if deleted_expense.user_id != current_user.id:
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
