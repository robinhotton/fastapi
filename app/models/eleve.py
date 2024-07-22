from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime

class Eleve(BaseModel):
    id: Optional[str] = Field(alias="_id")
    nom: str
    prenom: str
    classe: str
    date_naissance: datetime
    adresse: Optional[str]
    sexe: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
