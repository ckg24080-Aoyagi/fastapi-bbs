from fastapi import APIRouter

router = APIRouter(
    prefix="/threads",
    tags=["Threads"],  # Swaggerでのグループ名
)