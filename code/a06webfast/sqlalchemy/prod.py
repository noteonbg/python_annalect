from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List

# Step 1: Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./manufacturing.db"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for the models
Base = declarative_base()
'''
declarative_base() creates a base class for all SQLAlchemy models.
 Any model (e.g., Product) will inherit from Base to become part 
 of the database schema.
'''



# Step 2: Define the Product model (table)
class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    quantity_in_stock = Column(Integer)

# Step 3: Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 4: Create the tables in the database
Base.metadata.create_all(bind=engine)

# Step 5: Pydantic models for data validation
class ProductCreate(BaseModel):
    name: str
    description: str
    quantity_in_stock: int

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True

        '''
        orm_mode = True is crucial because it tells Pydantic to treat the
          SQLAlchemy model as a dictionary,
            SQLAlchemy models to JSON.
        '''

# Step 6: Initialize FastAPI app
app = FastAPI()

# Step 7: Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Step 8: CRUD Operations
# Create a product
@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, description=product.description, quantity_in_stock=product.quantity_in_stock)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get all products
@app.get("/products/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# Get a single product by ID
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Update a product
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_product.name = product.name
    db_product.description = product.description
    db_product.quantity_in_stock = product.quantity_in_stock
    
    db.commit()
    db.refresh(db_product)
    return db_product

# Delete a product
@app.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return db_product
