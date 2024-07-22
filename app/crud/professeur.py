from app.database import db
from pymongo.collection import Collection
from bson import ObjectId

collection: Collection = db["professeurs"]

def convert_object_ids(document):
    """Convert ObjectId to str in a MongoDB document."""
    if "_id" in document:
        document["_id"] = str(document["_id"])
    return document

def get_all_professeurs():
    professeurs = list(collection.find())
    return [convert_object_ids(professeur) for professeur in professeurs]
