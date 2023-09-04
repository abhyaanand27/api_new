from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/Moviename/received")
def read_name():
    return {"message": "GET request to retrieve Movie name"}

@app.post("/Moviename/search")
def read_name():
    return {"message": "Post request to send Movie name"}

@app.get("/Moviename/getBackend")
def read_name():
    return {"message": "GET request to retrieve movie name for backend"}

@app.post("/Moviename/postBackend")
def read_name():
    return {"message": "POST request to send final sentiment alalysis back to API"}


