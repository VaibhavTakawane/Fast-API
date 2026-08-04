from fastapi import FastAPI

from app.routes import app_router
import app.models
from app.db.session import Base
from app.db.database import engine


Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(app_router)
