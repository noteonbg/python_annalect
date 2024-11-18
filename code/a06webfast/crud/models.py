from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int]  # ID is optional for creating a product, but will be generated automatically
    name: str
    description: Optional[str] = None
    price: float
    quantity_in_stock: int

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity_in_stock: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity_in_stock: Optional[int] = None
