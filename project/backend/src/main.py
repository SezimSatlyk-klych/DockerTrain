import os
from fastapi import FastAPI

app = FastAPI()

MY_PROJECT = os.environ.get("MY_PROJECT") or "this is my project"
API_KEY = os.environ.get("API_KEY")


@app.get("/")
def read_index():
    return {"Hello": "World","project_name": API_KEY}