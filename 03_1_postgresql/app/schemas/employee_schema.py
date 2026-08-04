from pydantic import BaseModel, Field, EmailStr


class EmployeeRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    department: str = Field(..., min_length=2)
    salary: float = Field(..., gt=0)


class EmployeeResponse(BaseModel):
    id : int
    name : str
    email : str
    department : str
    salary : float