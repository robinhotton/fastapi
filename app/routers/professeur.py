from fastapi import APIRouter, HTTPException
from app.crud import professeur as crud
from app.schemas.professeur import ProfesseurUpdateSchema, ProfesseurCreateSchema

router = APIRouter(tags=["Professeurs"], prefix="/professeurs")

@router.get("/")
def get_all_professeurs():
    # Récupérer tous les professeurs
    professeurs = crud.get_all_professeurs()
    if not professeurs:
        return {"message": "No professors found."}
    return professeurs

@router.get("/{professeur_id}")
def get_professeur_by_id(professeur_id: str):
    # Récupérer un professeur par ID
    professeur = crud.get_professeur_by_id(professeur_id)
    if professeur is None:
        raise HTTPException(status_code=400, detail=f"{professeur_id} is not a valid ObjectId or Professeur not found.")
    return professeur

@router.post("/")
def create_professeur(professeur: ProfesseurCreateSchema):
    try:
        created_professeur = crud.create_professeur(professeur.dict(exclude_unset=True))
        return {"message": "Professeur created successfully", **created_professeur}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{professeur_id}")
def update_professeur_by_id(professeur_id: str, update: ProfesseurUpdateSchema):
    # Mettre à jour un professeur par ID
    print(update)
    result = crud.update_professeur_by_id(professeur_id, update)
    if result is None:
        raise HTTPException(status_code=400, detail=f"{professeur_id} is not a valid ObjectId")
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Professeur not found.")
    return {"message": "Professeur updated successfully", "matched_count": result.matched_count, "modified_count": result.modified_count}

@router.delete("/{professeur_id}")
def delete_professeur_by_id(professeur_id: str):
    # Supprimer un professeur par ID
    result = crud.delete_professeur_by_id(professeur_id)
    if result is None:
        raise HTTPException(status_code=400, detail=f"{professeur_id} is not a valid ObjectId")
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Professeur not found.")
    return {"message": "Professeur deleted successfully", "deleted_count": result.deleted_count}
