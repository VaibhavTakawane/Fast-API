import time
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI()
# -----------------------------------------------------------------------


# @app.get("/")
# def read_root():
#     return {"Hello": "vaibhav",'sirName' : 'Takawane'}

# @app.get("/about")
# def read_root():
#     return {'message' : 'This is about page'}
# -----------------------------------------------------------------------

# dynamic route
# @app.get("/user/{user_id}/")
# def get_user(user_id):
#     return {'user_id': user_id}

# dynamic route based on data type
# @app.get("/user/{user_id}/")
# def get_user(user_id:str):
#     return {"user_id": user_id}
# -----------------------------------------------------------------------------------

# QUERY PARAMETERS:
# 1.OPTIONAL PARAMS:
# @app.get('/products/')
# def get_products(name: str = None):
#     return {
#         'name': name,
#     }
# ----------------------------------
# 2.DEFAULT VALUES:
# @app.get('/products/')
# def get_products( limit: int = 20):
#     return {
#         'limit': limit
#     }
# ----------------------------------
# 3.MULTIPLE QUERY PARAMS:
# @app.get('/products/')
# def get_products(name: str = None, limit: int = 20):
#     return {
#         'name': name,
#         'limit': limit
#     }
# -----------------------------------------------------------------------------------

# POST:
# REQUEST BODY :
# 1.
# @app.post('/user/')
# def create_user(user:dict):
#     return {
#         'msg': "user is created",
#         "data": user
#     }
# -----------------------------------------------------------------------------------
# 2.PYDANTIC:
# a.schema, b.data validation, c.nested models
# class Address(BaseModel):
#     city: str
#     state: str
# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#     address: Address

# @app.post('/create_user/')
# def create_user(user: User):
# return {
#     'msg': "user is created",
#     "data": user
# }
# -----------------------------------------------------------------------------------

# CRUD:
# 1.CREATE:
# todos = []
# class Todo(BaseModel):
#     id: int
#     Title: str
#     complete: bool

# @app.post("/todos")
# def create_todos(todo: Todo):
#     todos.append(todo)
#     return {
#         "message": "todo created",
#         "todo": todo
#     }
# # ------------------------------------------------
# @app.get("/todos")
# def get_todos():
#     return todos
# # ------------------------------------------------
# @app.get("/todos/{t_id}")
# def get_one_todo(t_id: int):
#     for todo in todos:
#         if t_id == todo.id:
#             return todo
#     return {"error": "todo NOT FOUND"}
# # ------------------------------------------------
# UPDATE:
# @app.put("/todos/{t_id}")
# def update_todo(t_id: int, todo: Todo):
#     for i, t in enumerate(todos):
#         if t_id == t.id:
#             todos[i] = todo
#             return {
#                 "message": "DATA UPDATED",
#                 "data": todo
#             }
#     return {"error": "todo NOT FOUND TO UPDATE"}
# # ------------------------------------------------
# DELETE:
# @app.delete("/todos/{t_id}/")
# def delete_todo(t_id: int):
#     for i, t in enumerate(todos):
#         print(i, '==>', t)
#         if t_id == t.id:
#             rem = todos.pop(i)
#             return {
#                 "message": "todo REMOVED DONE",
#                 "data": rem}
#     return {"message": "todo OT FOUND"}
# -----------------------------------------------------------------------------------

# RESPONSE MODEL: => use to hide the data from frontend

# class User(BaseModel):
#     name: str
#     age: int
#     password: str


# class UserResponse(BaseModel):
#     name: str
#     age: int

# @app.get("/user", response_model=UserResponse)
# def get_user():
#     return {
#         "name": "ram",
#         "age": 20,
#         "password": "asdf",
#     }
# -----------------------------------------------------------------------------------
# STATUS CODES & RESPONSES:
# 1.http status codes
# 2.custom responses
# 3.error handling

# 1.http status codes:
# @app.post("/user/", status_code=status.HTTP_201_CREATED)
# def create_user():
#     return{
#         "msg":"user created",
#     }
# ------------------------------------------------
# 3.error handling:
# @app.get("/user/{u_id}")
# def get_user(u_id:int):
#     if u_id != 1:
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND,
#             detail = "user not fount"
#         )
#     return{
#         "data":"ram",
#         "age":20
#     }
# -----------------------------------------------------------------------------------
# EXCEPTION HANDLING:
# 1.HTTPException
# 2.CUSTON Exceptions
# 3.GLOBAL ERROR HANDLING

# from fastapi import Request
# from fastapi.responses import JSONResponse
# class UserNotFoundException(Exception):     #Custom exception
#     def __init__(self, name:str):
#         self.name = name

# @app.exception_handler(UserNotFoundException)
# def user_notfound_handler(reques=Request, exc=UserNotFoundException):        #Global exception handler function
#     return JSONResponse(
#         status_code=404,
#         content={
#             "status":"ERROR",
#             "message": f"User {exc.name} not found"
#         }
#     )

# @app.get("/user/{name}")
# def get_user(name):
#     if name != "ram":
#         raise UserNotFoundException(name)
#     return {
#         "name" : name
#     }

# -----------------------------------------------------------------------------------
# DEPENDENCY INJECTIONS: => it is a design pattern which provides a dependency to a function externally.
# 1.WHAT IS DEPENDS() => CALL A FUNCTION automatic and inject the result of this function in another function .
# 2.REUSABLE LOGIC

# from fastapi import Depends

# def current_user():
#     return{
#         "user":"ram"
#     }

# @app.get("/profile/")
# def get_profile(curr_user=Depends(current_user)):
#     return curr_user

# @app.get("/dashobard/")
# def get_dashobard(curr_user=Depends(current_user)):
#     return curr_user
# ------------------------------------------------
# 3.AUTH EXAMPLE INTRO:
# from fastapi import HTTPException, Depends, Header

# def varify_token(token:str = Header(None)):
#     if token != "abcd123":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="unauthorized user"
#         )
#     return{
#         "user":"Authorised User"
#     }

# @app.get("/secure-data/")
# def secure_data(user=Depends(varify_token)):
#     return{
#         "message":"secure data accessed",
#         "user":user
#     }


# -----------------------------------------------------------------------------------
# MIDDLEWARE:
# from fastapi import Request
# @app.middleware("http")
# async def get_time(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     end_time = time.time() - start_time
#     print(f"Path:{request.url.path} || Time : {end_time}")
#     return response
# -----------------------------------------------------------------------------------

# ------------------------------------------------
# ------------------------------------------------