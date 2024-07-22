from app.database import db
from pymongo.collection import Collection

collection: Collection = db["professeurs"]

def get_all_professeurs():
    return list(collection.find())