from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from dotenv import load_dotenv
# import os

# load_dotenv()

from config import settings

app = FastAPI()
 
#allowed origins (frontend url)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,  # allowed FE
    allow_credentials=[True],   
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def home():
    return {
        "message": "CORS api handling",
        "allowed_origins": settings.origins,
        "secret_key": settings.secret_key
}
