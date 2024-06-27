"""
Main aplication module
"""

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
import psycopg2
from psycopg2.extras import RealDictCursor
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from routers import posts, users, auth, expenses, expensecategories, budget


models.Base.metadata.create_all(bind=engine)

# try:
#     conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='password', cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection successfull")
# except Exception as error:
#     print("Database connection failed")
#     print("Error", error)

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool


# my_posts = [{"title" : "first title", "content": "another content", "id": 1}, {"title": "second title", "content": "I like pizzaa", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p

# CREATING THE LOGIC BEHIND THE EXPENSE AND THE BUDGET AND WHEN THE USER GETS NOTIFIED ABOUT THEIR EXPENSE HABITS
# UPDATING THE SETTINGS AND ALSO TRY ADDING A DARK THEME LINKED WITH BACKEND AND SAVING THE USER'S THEME ON THE BACKEND(EITHER LIGHT OR DARK)
# UPDATING THAT NOTIFICATION UI ON THE SIDEBAR MENU
# UPDATING THE GRAPHS
# IMPLEMENTIMG LOG OUT AND DEACTIVATION FUNTIONALITY
# EXPENSE LIST AND BUDGET LIST PAGE
# GENERATING REPORT FOR THE EXPENSE IN A MONTH
# OPTIONAL: •	Allow users to export their data to CSV or Excel files.
#           •	Provide functionality to import data, which is useful if they switch devices or want to integrate with other applications.



app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(expenses.router)
app.include_router(expensecategories.router)
app.include_router(budget.router)