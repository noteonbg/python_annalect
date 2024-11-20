from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI app
app = FastAPI()

# In-memory storage (simulating a database)
products_db = {}

# Pydantic model to define the structure of Product
class Product(BaseModel):
    name: str
    price: float

# Create a product
@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    # Generate productid automatically (for simplicity, using an incremental integer)
    productid = len(products_db) + 1
    products_db[productid] = product
    return product

# Read all products
@app.get("/products/", response_model=List[Product])
async def get_products():
    return list(products_db.values())

# Read a product by productid
@app.get("/products/{productid}", response_model=Product)
async def get_product(productid: int):
    product = products_db.get(productid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Update a product by productid
@app.put("/products/{productid}", response_model=Product)
async def update_product(productid: int, product: Product):
    if productid not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db[productid] = product
    return product

# Delete a product by productid
@app.delete("/products/{productid}", response_model=Product)
async def delete_product(productid: int):
    product = products_db.pop(productid, None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
