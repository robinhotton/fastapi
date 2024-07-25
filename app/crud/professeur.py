from app.database import db
from pymongo.collection import Collection
from bson import ObjectId
from bson.errors import InvalidId
from typing import List

collection: Collection = db["professeurs"]

def get_all_professeurs():
    # Récupérer tous les professeurs sans l'_id
    return list(collection.find({}, {"_id": 0}))

def get_professeur_by_id(professeur_id: str):
    try:
        # Convertir l'ID en ObjectId
        professeur = collection.find_one({"_id": ObjectId(professeur_id)}, {"_id": 0})
        return professeur
    except InvalidId:
        return None

def create_professeur(professeur: dict):
    try:
        # Insérer le professeur dans la collection
        result = collection.insert_one(professeur)
        print("create_professeur", result)
        return {"_id": str(result.inserted_id)}
    except Exception as e:
        raise e

def update_professeur_by_id(professeur_id: str, update: dict):
    try:
        # Mettre à jour le professeur par ID
        result = collection.update_one({"_id": ObjectId(professeur_id)}, {"$set": update})
        return result
    except InvalidId:
        return None

def delete_professeur_by_id(professeur_id: str):
    try:
        # Supprimer le professeur par ID
        result = collection.delete_one({"_id": ObjectId(professeur_id)})
        return result
    except InvalidId:
        return None
