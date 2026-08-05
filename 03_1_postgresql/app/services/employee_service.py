from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.employee_model import Employees

def get_employee_service(db:Session):
    employees = db.query(Employees).all()
    return employees

def get_employee_by_id_service(db:Session, e_id: int):
    employee = db.query(Employees).filter(Employees.id == e_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee 


# def create_employee_service(db: Session, emp_data:dict):
#     new_employee = Employees(**emp_data)
#     db.add(new_employee)
#     db.commit()
#     db.refresh(new_employee)
#     return new_employee


def create_employee_service(db: Session, emp_data: dict):
    # Check if email already exists
    existing_employee = (
        db.query(Employees)
        .filter(Employees.email == emp_data["email"])
        .first()
    )
    if existing_employee:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    # Create new employee
    new_employee = Employees(**emp_data)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee_service(db:Session, e_id:int, emp_data:dict):
    employee = db.query(Employees).filter(Employees.id == e_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in emp_data.items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee_service(db:Session, e_id:int):
    employee = db.query(Employees).filter(Employees.id == e_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
    return {"message": "Employee deleted successfully"}
