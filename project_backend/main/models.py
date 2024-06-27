from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float, JSON
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Date
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from datetime import datetime

class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='NO ACTION'), nullable=False)

    user = relationship("Users", back_populates="posts")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")  # e.g., admin, user
    is_active = Column(Boolean, nullable=False, default=True)
    expenses = relationship("Expense", back_populates="user")
    budgets = relationship("Budget", back_populates="user")
    # notifications = relationship("Notification", back_populates="user")
    # reports = relationship("Report", back_populates="user")
    posts = relationship("Posts", back_populates="user")


class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    amount = Column(Float)
    category = Column(String, index=True)
    payment_method = Column(String)
    start_date = Column(DateTime, index=True)
    end_date = Column(DateTime, index=True)
    description = Column(String, nullable=True)

    user = relationship("Users", back_populates="expenses")


class Budget(Base):
    __tablename__ = 'budgets'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    category = Column(String)
    amount = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime, nullable=True)
    notification_preferences = Column(String)
    roll_over = Column(Boolean)

    user = relationship("Users", back_populates="budgets")
    # notifications = relationship("Notification", back_populates="budget")


# class Report(Base):
#     __tablename__ = 'reports'
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     start_date = Column(DateTime)
#     end_date = Column(DateTime)
#     total_expense = Column(Float)
#     category_breakdown = Column(JSON)

#     user = relationship("User", back_populates="reports")


# class ExpenseSummary(Base):
#     __tablename__ = 'expense_summaries'
    
#     budget_id = Column(Integer, ForeignKey('budgets.id'), primary_key=True)
#     total_spent = Column(Float)
#     percentage_used = Column(Float)


# class ExpenseCategory(Base):
#     __tablename__ = "expense_categories"

#     id = Column(Integer, primary_key=True, nullable=False)
#     name = Column(String, nullable=False, unique=True)
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # user = relationship("User", back_populates="categories")


# class Budget(Base):
#     __tablename__ = "budgets"

#     id = Column(Integer, primary_key=True, nullable=False)
#     amount = Column(Integer, nullable=False)
#     start_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     end_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # user = relationship("User", back_populates="budgets")
    # type = Column(Enum(BudgetType), nullable=False)
    # expenses = relationship("Expense", back_populates="budget")

# class UserSettings(Base):
#     __tablename__ = "user_settings"

#     id = Column(Integer, primary_key=True, nullable=False)
#     notification_preferences = Column(String, nullable=True)
    # user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # user = relationship("User", back_populates="settings")

class TokenBlacklist(Base):
    __tablename__ = 'token_blacklist'
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, index=True, unique=True)
    blacklisted_on = Column(DateTime, default=datetime.utcnow)