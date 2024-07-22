from typing import List
from pymongo.collection import Collection
from bson import ObjectId  # Add this import
from app.database import db
from app.models.eleve import Eleve

collection: Collection = db["eleves"]

def get_all_eleves() -> List[Eleve]:
    return list(collection.find({}, {"_id": 1, "nom": 1, "prenom": 1, "classe": 1, "date_naissance": 1, "adresse": 1, "sexe": 1}))

def get_eleve(eleve_id: str) -> Eleve:
    return collection.find_one({"_id": ObjectId(eleve_id)})

def create_eleve(eleve: Eleve) -> Eleve:
    result = collection.insert_one(eleve.dict(by_alias=True))
    return get_eleve(result.inserted_id)

def update_eleve(eleve_id: str, eleve: Eleve) -> Eleve:
    collection.update_one({"_id": ObjectId(eleve_id)}, {"$set": eleve.dict(by_alias=True)})
    return get_eleve(eleve_id)

def delete_eleve(eleve_id: str) -> bool:
    result = collection.delete_one({"_id": ObjectId(eleve_id)})
    return result.deleted_count > 0
