from sqlalchemy.orm import Session

from app.services.employee_service import *

def get_employee_controller(db:Session):
    return get_employee_service(db)

def get_employee_by_id_controller(db:Session, e_id:int):
    return get_employee_by_id_service(db, e_id)


def create_employee_controller(db:Session, emp_data):
    return create_employee_service(db,emp_data.model_dump())

def update_employee_controller(db:Session, e_id:int, emp_data):
    return update_employee_service(db, e_id, emp_data.model_dump())