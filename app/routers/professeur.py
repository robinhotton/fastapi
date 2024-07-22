from fastapi import APIRouter
from app.crud import professeur as crud

router = APIRouter(tags=["Professeurs"], prefix="/professeurs")

@router.get("/")
def get_all_professeurs():
    return crud.get_all_professeurs()
