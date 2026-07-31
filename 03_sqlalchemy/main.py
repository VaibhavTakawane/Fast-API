# FIRST INSTALL : pip install SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker, declarative_base

from fastapi import FastAPI, Depends, HTTPException, status

from config import settings

app = FastAPI()

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
# -----------------------------------------------
# CREATE:

@app.post("/todos/")
def create_todo(title: str, db: Session  = Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo created",
        "data": todo
    }
# -----------------------------------------------
# GET/FETCH/READ ALL TODOS:

@app.get("/todos/")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return {
        "message": "data fetched successfully",
        "total": len(todos),
        "data": todos
    }
# -----------------------------------------------

# GET/FETCH/READ SINGLE TODO_ BY ID:

@app.get("/todo/{t_id}/")
def get_todo(t_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(t_id == Todo.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {
        "message": "data fetched successfully",
        "data": todo
    }
# ------------------------------------------------
# PUT/UPDATE:
@app.put("/todos/{t_id}/")
def update_todo(t_id: int, title: str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(t_id == Todo.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = title
    db.commit()
    db.refresh(todo)
    return {
        "message": "data updated successfully",
        "data": todo
    }
# ------------------------------------------------


@app.delete("/todo/{t_id}/")
def delete_todo(t_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(t_id == Todo.id).first()
    db.delete(todo)
    db.commit()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {
        "message": "data delete successfully"
    }
# ----------------------------------------------------------------------------------------------
