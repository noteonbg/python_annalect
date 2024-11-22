#python -m uvicorn a01app:app --reload

from fastapi import FastAPI, HTTPException, status
from typing import Optional

# Create an instance of FastAPI
app = FastAPI()

# Route to add two numbers via query parameters
@app.get("/sum_query", status_code=status.HTTP_200_OK)
#below function will now not react to http event..why we did not register for the event
def sum_query(a: int, b: int):
    """
    This endpoint takes two numbers as query parameters and returns their sum.
    Example: /sum_query?a=5&b=10
    """
    if a is None or b is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both 'a' and 'b' query parameters are required"
        )
    return {"sum": a + b}

# Route to add two numbers via path variables
@app.get("/sum_path/{a}/{b}", status_code=status.HTTP_200_OK)
def sum_path(a: int, b: int):
    """
    This endpoint takes two numbers as path variables and returns their sum.
    Example: /sum_path/5/10
    """
    if a is None or b is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both 'a' and 'b' path variables are required"
        )
    return {"sum": a + b}

# Example of a route with error handling
@app.get("/divide/{a}/{b}", status_code=status.HTTP_200_OK)
def divide(a: int, b: int):
    """
    This endpoint divides a by b and returns the result.
    Example: /divide/10/2
    """
    if b == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Division by zero is not allowed"
        )
    return {"result": a / b}

    '''steps

    python -m venv fastapi
    Set-ExecutionPolicy Unrestricted -Scope Process
    .\fastapi\Scripts\activate
    pip install fastapi uvicorn

    

    
    '''
