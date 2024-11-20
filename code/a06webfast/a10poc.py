from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# Define a simple model for demonstration
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Route for 200 OK (Success)
@app.get("/ok", status_code=status.HTTP_200_OK)
async def read_item():
    return {"message": "Everything is OK!", "status_code": 200}

# Route for 201 Created (Successful creation)
@app.post("/create", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return {"message": f"Item '{item.name}' created successfully!", "status_code": 201}

# Route for 400 Bad Request (Client Error)
@app.post("/bad-request", status_code=status.HTTP_406_NOT_ACCEPTABLE)
async def bad_request(item: Item):
    if item.price < 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="inputs cannot be zero."
        )
    return {"message": "Item is valid.", "status_code": 200}

# Route for 404 Not Found (Resource not found)
@app.get("/not-found/{item_id}", status_code=status.HTTP_404_NOT_FOUND)
async def not_found(item_id: int):
    # Simulating resource not found for demonstration
    if item_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found."
        )
    return {"message": "Item found.", "status_code": 200}

# Route for 409 Conflict (Conflict in resource state)
@app.put("/conflict/{item_id}", status_code=status.HTTP_409_CONFLICT)
async def conflict(item_id: int, item: Item):
    # Simulating a conflict situation where item ID 1 already exists
    if item_id == 1:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Item with id {item_id} already exists. Cannot update."
        )
    return {"message": f"Item {item_id} updated successfully.", "status_code": 200}

# Route for 500 Internal Server Error (Server error)
@app.get("/server-error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
async def server_error():
    # Simulating an internal server error
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal server error. Something went wrong."
    )

# Route for 503 Service Unavailable (Service temporarily unavailable)
@app.get("/service-unavailable", status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
async def service_unavailable():
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Service is temporarily unavailable. Please try again later."
    )

