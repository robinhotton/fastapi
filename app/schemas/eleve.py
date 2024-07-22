from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EleveCreate(BaseModel):
    nom: str
    prenom: str
    classe: str
    date_naissance: datetime
    adresse: Optional[str]
    sexe: str

class Eleve(EleveCreate):
    id: str
