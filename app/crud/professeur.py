from app.database import db
from pymongo.collection import Collection
from bson import ObjectId

collection: Collection = db["professeurs"]

def get_all_professeurs():
    professeurs = collection.find({}, {"_id": 0})
    return list(professeurs)

def get_professeur(professeur_id: str):
    professeur = collection.find_one({"_id": ObjectId(professeur_id)}, {"_id": 0})
    return professeur