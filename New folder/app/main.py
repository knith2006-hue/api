from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Hello World"}

class data(BaseModel):
    id:int
    name:str
    age:int
    email:str

ls=[]
@app.post("/post")
def post_data(data:data):
    ls.append(data.dict())
    return {"message":"Hello World"}

@app.get("/get")
def get_data():
     return dict(ls)

@app.get("/get/{id}")
def a(id:int):
    for i in ls:
        if i["id"]==id:
            return i
    return {"message":"Not Found"}

