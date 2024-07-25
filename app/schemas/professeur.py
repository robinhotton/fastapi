from datetime import date
from pydantic import BaseModel, constr
from typing import Optional

class ProfesseurUpdateSchema(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    date_naissance: Optional[date] = None
    adresse: Optional[str] = None
    sexe: Optional[str] = None

class ProfesseurCreateSchema(BaseModel):
    nom: str = constr(min_length=1)
    prenom: str = constr(min_length=1)
    date_naissance: date
    adresse: str = constr(min_length=1)
    sexe: str = constr(min_length=1)
