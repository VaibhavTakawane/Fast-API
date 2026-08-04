from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.controllers.employee_controller import *
from app.schemas.employee_schema import EmployeeResponse, EmployeeRequest

router = APIRouter()


@router.get("/", response_model=list[EmployeeResponse])
def get_employee(db: Session = Depends(get_db)):
    return get_employee_controller(db)


@router.get("/{e_id}", response_model=EmployeeResponse)
def get_employee_by_id(e_id: int, db: Session = Depends(get_db)):
    return get_employee_by_id_controller(db, e_id)


@router.post("/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeRequest, db: Session = Depends(get_db)):
    return create_employee_controller(db, employee)

@router.put("/{e_id}", response_model=EmployeeResponse)
def update_employee(e_id: int, employee: EmployeeRequest, db: Session = Depends(get_db)):
    return update_employee_controller(db, e_id, employee)