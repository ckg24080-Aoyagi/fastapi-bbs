from fastapi import FastAPI
from app.routers import threads
from app.routers import posts  # ← 追加

app = FastAPI(title="BBS API")

# Threadsルーターを登録
app.include_router(threads.router)
app.include_router(posts.router)
app.include_router(posts.threads_router)