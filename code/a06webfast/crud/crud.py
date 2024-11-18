from typing import List, Optional
from models import Product, ProductCreate, ProductUpdate

# In-memory "database" as a list
fake_db: List[Product] = []

def get_products(skip: int = 0, limit: int = 10) -> List[Product]:
    """Retrieve a list of products with pagination."""
    return fake_db[skip : skip + limit]

def get_product_by_id(product_id: int) -> Optional[Product]:
    """Retrieve a product by its ID."""
    return next((product for product in fake_db if product.id == product_id), None)

def create_product(product_create: ProductCreate) -> Product:
    """Create a new product and add it to the fake database."""
    product_id = len(fake_db) + 1  # Simple id generation based on list length
    new_product = Product(id=product_id, **product_create.model_dump())
    fake_db.append(new_product)
    return new_product

def update_product(product_id: int, product_update: ProductUpdate) -> Optional[Product]:
    """Update an existing product."""
    product = get_product_by_id(product_id)
    if product:
        updated_data = product.model_dump(exclude_unset=True)
        updated_data.update(product_update.model_dump(exclude_unset=True))
        updated_product = Product(**updated_data)
        
        # Replace the old product with the updated one
        fake_db[fake_db.index(product)] = updated_product
        return updated_product
    return None

def delete_product(product_id: int) -> Optional[Product]:
    """Delete a product by its ID."""
    product = get_product_by_id(product_id)
    if product:
        fake_db.remove(product)
        return product
    return None
