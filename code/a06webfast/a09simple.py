from fastapi import FastAPI, HTTPException
from fastapi import status
from typing import Dict

# Define a simple class for Rectangle
class Rectangle:
    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth

    def validate(self):
        # Ensure that the length and breadth are positive
        if self.length <= 0 or self.breadth <= 0:
            raise ValueError("Length and breadth must be positive values.")

# Define a simple class for PA (Area and Perimeter)
class PA:
    def __init__(self, area: float, perimeter: float):
        self.area = area
        self.perimeter = perimeter

    def to_dict(self):
        # Convert the object to a dictionary for the JSON response
        return {"area": self.area, "perimeter": self.perimeter}

# Initialize FastAPI app
app = FastAPI()

@app.post("/poc")
async def poc(pa):
    print("hope this works")
    return pa





@app.post("/calculate", status_code=status.HTTP_200_OK)
async def calculate_pa(rectangle):
    try:
        # Validate the rectangle dimensions
        rectangle.validate()

        # Calculate the area and perimeter
        area = rectangle.length * rectangle.breadth
        perimeter = 2 * (rectangle.length + rectangle.breadth)

        
        pa = PA(area=area, perimeter=perimeter)# we are creating an object of the class PA

        # Return the PA object as a dictionary
        return pa.to_dict()

    except ValueError as e:
        # If validation fails, raise a 400 Bad Request
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
