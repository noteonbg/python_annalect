#python -m uvicorn a01app:app --reload

from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Product, ProductCreate, ProductUpdate
import crud

app = FastAPI()

@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product_create: ProductCreate):
    """Create a new product."""
    new_product = crud.create_product(product_create)
    return new_product

@app.get("/products/", response_model=List[Product], status_code=status.HTTP_200_OK)
async def get_products(skip: int = 0, limit: int = 10):
    """Retrieve products with pagination."""
    products = crud.get_products(skip, limit)
    return products

@app.get("/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
async def get_product(product_id: int):
    """Get a single product by ID."""
    product = crud.get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@app.put("/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product_update: ProductUpdate):
    """Update a product by its ID."""
    updated_product = crud.update_product(product_id, product_update)
    if not updated_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return updated_product

@app.delete("/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
async def delete_product(product_id: int):
    """Delete a product by its ID."""
    deleted_product = crud.delete_product(product_id)
    if not deleted_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return deleted_product
