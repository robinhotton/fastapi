from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.eleve import Eleve, EleveCreate
from app.crud import eleve as crud

router = APIRouter(
    prefix="/eleves",
    tags=["eleves"]
)

@router.get("/", response_model=List[Eleve])
def read_eleves():
    return crud.get_all_eleves()

@router.get("/{eleve_id}", response_model=Eleve)
def read_eleve(eleve_id: str):
    eleve = crud.get_eleve(eleve_id)
    if eleve is None:
        raise HTTPException(status_code=404, detail="Eleve not found")
    return eleve

@router.post("/", response_model=Eleve)
def create_eleve(eleve: EleveCreate):
    return crud.create_eleve(Eleve(**eleve.dict()))

@router.put("/{eleve_id}", response_model=Eleve)
def update_eleve(eleve_id: str, eleve: EleveCreate):
    return crud.update_eleve(eleve_id, Eleve(**eleve.dict(), id=eleve_id))

@router.delete("/{eleve_id}", response_model=bool)
def delete_eleve(eleve_id: str):
    return crud.delete_eleve(eleve_id)
