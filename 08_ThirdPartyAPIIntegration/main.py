# FETCH DATA BY PYTHON:

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = response.json()
# print(data)
# ------------------------------------------------------------------------------------

from fastapi import FastAPI
import requests

app = FastAPI()

#all posts
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.get(url)
    return response.json()

#single post
@app.get("/post/{p_id}")
def get_post(p_id: int):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{p_id}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"ERROR": str(e)}