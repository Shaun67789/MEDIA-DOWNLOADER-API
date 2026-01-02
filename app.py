from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from engine import execute
from cleanup import start_cleaner
from keep_alive import start_keep_alive
from config import BASE_URL
import os

app = FastAPI()

start_cleaner()
start_keep_alive(BASE_URL)

@app.post("/execute")
def run(payload: dict):
    return execute(payload)

@app.get("/file/{name}")
def file(name: str, bg: BackgroundTasks):
    path = f"downloads/{name}"
    if not os.path.exists(path):
        raise HTTPException(404)
    bg.add_task(os.remove,path)
    return FileResponse(path, filename=name)