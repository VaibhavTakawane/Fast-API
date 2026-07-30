from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allowed origins (frontend url)
origins = [
    "http://localhost:5173",  # React app's origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allowed FE
    allow_credentials=[True],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
def home():
    return {"message": "Hello, World! how are you"}
