from fastapi import APIRouter
from app.routes.employee_route import router as employee_router

app_router = APIRouter()

app_router.include_router(
    employee_router, prefix="/employee", tags=["employee"])
