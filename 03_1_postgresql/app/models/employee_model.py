from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Employees(Base):
    __tablename__ = "employees"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    email = Column(String,unique=True)
    department = Column(String)
    salary = Column(Integer)
    