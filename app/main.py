from fastapi import FastAPI
from app.routers import threads

app = FastAPI(title="BBS API")

# Threadsルーターを登録
app.include_router(threads.router)