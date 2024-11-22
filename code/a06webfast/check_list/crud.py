from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task

DATABASE_URL = "sqlite:///./test.db"  # SQLite Database

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
SessionLocal: This is the sessionmaker instance that will interact with the SQLite database.
Base.metadata.create_all(bind=engine): This creates all tables based on the defined models.

"""
# Create the tables in the database
Base.metadata.create_all(bind=engine)

# CRUD Operations
def get_task(db, task_id: int):
    return db.query(Task).filter(Task.task_id == task_id).first()

def get_tasks(db, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def create_task(db, task_name: str, status: str, location: str):
    db_task = Task(task_name=task_name, status=status, location=location)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db, task_id: int, status: str):
    db_task = db.query(Task).filter(Task.task_id == task_id).first()
    if db_task:
        db_task.status = status
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db, task_id: int):
    db_task = db.query(Task).filter(Task.task_id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None
