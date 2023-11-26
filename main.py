from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def f_index():
    return "Hello! I'm Oplachko Vadim Romanovich, nice too meet you"

@app.get("/tools")
async def f_indexT():
    return "Я посредственно знаю английский язык, но умею программировать на питоне, знаю Django, работаю с PyQt"

@app.get("/users")
async def f_indexT():
    return "+79628187055 is my phone number"
