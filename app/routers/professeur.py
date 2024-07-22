from fastapi import APIRouter
from app.crud import professeur as crud

router = APIRouter(tags=["Professeurs"], prefix="/professeurs")

@router.get("/")
def get_all_professeurs():
    return crud.get_all_professeurs()

@router.get("/{professeur_id}")
def get_professeur(professeur_id: str):
    return crud.get_professeur(professeur_id)