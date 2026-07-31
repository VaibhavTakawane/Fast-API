from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"result":"hello vaibhav"}

@app.get("/add/")
def home(a:int,b:int):
    return{"result":a+b}



