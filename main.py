from fastapi import FastAPI
from pydantic import BaseModel

from common.utils.text_filter import text_filters

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class TextMessage(BaseModel):
    text: str
    uid: str
    info: bool | None = None


class TextResult(BaseModel):
    message: TextMessage
    result: list
    block: bool


@app.post('/check/message', response_model=TextResult)
async def text_check(message: TextMessage):
    result = text_filters.check(message.text, message.info)
    return {
        'message': message,
        'result': result,
        'block': bool(result)
    }
