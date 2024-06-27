from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict
from typing import Optional
from datetime import datetime


# USERS LOGINS AND AUTHENTICATION
class UserCreate(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)

class UserOut(BaseModel):
    email: EmailStr
    id: int

    model_config = ConfigDict(from_attributes=True)

class login(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


# POST CREATION SCHEMAS
class Post(BaseModel):
    title: str
    content: str
    published: bool

    model_config = ConfigDict(from_attributes=True)

class PostResponse(Post):
    id: int
    user_id: int
    pass

    model_config = ConfigDict(from_attributes=True)


# EXPENSES CREATION SCHEMAS
class Expenses(BaseModel):
    amount: int
    description: str
    # category_id: int

    model_config = ConfigDict(from_attributes=True)

class ExpensesResponse(Expenses):
    pass

    model_config = ConfigDict(from_attributes=True)


class ExpenseCategory(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)

# BUDGET SCHEMAS

class BudgetIn(BaseModel):
    name: str
    category: str
    amount: float
    # time_period: str
    start_date: datetime
    end_date: Optional[datetime] = None
    notification_preferences: str
    roll_over: bool

class BudgetOut(BudgetIn):
    id: int
    user_id: int


# EXPENSE SCHEMAS
    
class ExpenseIn(BaseModel):
    name: str
    amount: float
    category: str
    payment_method: str
    # time_period: str
    start_date: datetime
    end_date: datetime
    description: str

class ExpenseOut(ExpenseIn):
    id: int
    user_id: int    

# USER SETTINGS SCHEMAS
class UserSettings(BaseModel):
    notification_preferences: str

    model_config = ConfigDict(from_attributes=True)