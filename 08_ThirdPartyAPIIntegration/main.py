# FETCH DATA BY PYTHON:

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = response.json()
# print(data)
# ------------------------------------------------------------------------------------

from fastapi import FastAPI
import requests

app = FastAPI()

# all posts
@app.get("/posts")
def get_posts(page: int = 1, limit: int = 5):
    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.get(url)
    data =  response.json()

    result = []
    for i in data:
        result.append(i)

        # result.append({
        #             "id": i["id"],                #to add specific data
        #             "title": i["title"]
        #         })

    # pagination logic:
    start = (page-1)*limit
    end = start + limit

    return {
                "page": page,
                "limit": limit,
                "Total": len(result),
                "data": result[start:end]
            }
# -----------------------------------

# single post
@app.get("/post/{p_id}")
def get_post(p_id: int):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{p_id}"
        response = requests.get(url)
        data = response.json()
        return data 
    except Exception as e:
        return {"ERROR": str(e)}
