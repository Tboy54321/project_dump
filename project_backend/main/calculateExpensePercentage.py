from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas

def check_budget_status(user_id: int, db: Session):
    budgets = db.query(models.Budget).filter(models.Budget.user_id == user_id).all()
    for budget in budgets:
        expenses = db.query(models.Expense).filter(
            models.Expense.user_id == user_id,
            models.Expense.category == budget.category,
            models.Expense.date >= budget.start_date,
            models.Expense.date <= budget.end_date
        ).all()

        total_expense = sum(expense.amount for expense in expenses)
        percentage_used = (total_expense / budget.amount) * 100

        if percentage_used > 100:
            message = f"You have exceeded your budget for {budget.category} within {budget.start_date} to {budget.end_date}."
        elif percentage_used > 80:
            message = f"You have used {percentage_used:.2f}% of your budget for {budget.category} within {budget.start_date} to {budget.end_date}."
        else:
            continue
        
        existing_notification = db.query(models.Notification).filter(
            # models.Notification.user_id == user_id,
            models.Notification.budget_id == budget.id,
            models.Notification.message == message,
            # models.Notification.date >= budget.start_date,
            # models.Notification.date <= budget.end_date
        ).first()

        if not existing_notification:
            notification = models.Notification(
                user_id=user_id,
                budget_id=budget.id,
                message=message,
                date=datetime.now(),
                read=False
            )
            db.add(notification)
            db.commit()
            db.refresh(notification)