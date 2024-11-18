# app.py

#python -m uvicorn a01app:app --reload

from fastapi import FastAPI
from typing import Optional

# Create an instance of FastAPI
app = FastAPI()

# Route to add two numbers via query parameters
@app.get("/sum_query")
def sum_query(a: int, b: int):
    """
    This endpoint takes two numbers as query parameters and returns their sum.
    Example: /sum_query?a=5&b=10
    """
    return {"sum": a + b}

# Route to add two numbers via path variables
@app.get("/sum_path/{a}/{b}")
def sum_path(a: int, b: int):
    """
    This endpoint takes two numbers as path variables and returns their sum.
    Example: /sum_path/5/10
    """
    return {"sum": a + b}
