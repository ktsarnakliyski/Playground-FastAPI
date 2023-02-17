from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UppercaseRequest(BaseModel):
    word: str


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.post("/uppercase")
def uppercase(request: UppercaseRequest):
    return {"word": request.word.upper()}
