from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models
from .crud import SessionLocal

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new task
@app.post("/tasks/", response_model=models.Task)
def create_task(task_name: str, status: str, location: str, db: Session = Depends(get_db)):
    return crud.create_task(db, task_name, status, location)

# Read all tasks
@app.get("/tasks/", response_model=list[models.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)

# Read a specific task by ID
@app.get("/tasks/{task_id}", response_model=models.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Update a task's status
@app.put("/tasks/{task_id}", response_model=models.Task)
def update_task(task_id: int, status: str, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_id, status)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Delete a task
@app.delete("/tasks/{task_id}", response_model=models.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

"""
Create a Task: POST /tasks/ with JSON body {"task_name": "Manufacturing Task 1", "status": "pending", "location": "Factory 1"}
Get All Tasks: GET /tasks/
Get a Specific Task: GET /tasks/{task_id}
Update a Task: PUT /tasks/{task_id} with JSON body {"status": "completed"}
Delete a Task: DELETE /tasks/{task_id}

"""