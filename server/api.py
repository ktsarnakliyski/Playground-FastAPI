from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UppercaseRequest(BaseModel):
    word: str


@app.get("/ping")
def hello_world():
    return {"message": "Pong!"}


@app.post("/uppercase")
def uppercase(request: UppercaseRequest):
    return {"word": request.word.upper()}
