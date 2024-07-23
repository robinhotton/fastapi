from app.database import db
from pymongo.collection import Collection
from bson import ObjectId

collection: Collection = db["professeurs"]

def get_all_professeurs():
    return list(collection.find({}, {"_id": 0}))

def get_professeur(professeur_id: str):
    return collection.find_one({"_id": ObjectId(professeur_id)}, {"_id": 0})

def get_professeur_by_filtre_projection(filtre: dict, projection: dict):
    professeurs = list(collection.find(filtre, projection))
    return professeurs

def create_professeur(professeur: dict):
    result = collection.insert_one(professeur)
    return {"_id": str(result.inserted_id)}

def update_professeur(professeur_id: str, professeur: dict):
    result = collection.update_one({"_id": ObjectId(professeur_id)}, {"$set": professeur})
    return {"matched_count": result.matched_count, "modified_count": result.modified_count}

def delete_professeur(professeur_id: str):
    result = collection.delete_one({"_id": ObjectId(professeur_id)})
    return {"deleted_count": result.deleted_count}