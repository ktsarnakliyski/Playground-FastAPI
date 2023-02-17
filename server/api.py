import uvicorn
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
