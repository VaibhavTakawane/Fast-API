from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

#now we are going to learn about cors: cross origin resource sharing