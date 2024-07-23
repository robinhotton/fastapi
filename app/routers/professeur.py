from fastapi import APIRouter
from app.crud import professeur as crud

router = APIRouter(tags=["Professeurs"], prefix="/professeurs")

@router.get("/")
def get_all_professeurs():
    return crud.get_all_professeurs()

@router.get("/{professeur_id}")
def get_professeur(professeur_id: str):
    return crud.get_professeur(professeur_id)

@router.post("/")
def create_professeur(professeur: dict):
    return crud.create_professeur(professeur)

@router.put("/{professeur_id}")
def update_professeur(professeur_id: str, professeur: dict):
    return crud.update_professeur(professeur_id, professeur)

@router.delete("/{professeur_id}")
def delete_professeur(professeur_id: str):
    return crud.delete_professeur(professeur_id)