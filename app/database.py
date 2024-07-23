# Importation des modules nécessaires
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Chargement des variables d'environnement
load_dotenv()
user = os.environ["USER"]
password = os.environ["PASSWORD"]
cluster = os.environ["CLUSTER"] 
database_name = os.environ["DB_NAME"]

# Encodage des caractères spéciaux dans le nom d'utilisateur et le mot de passe
encoded_user = quote_plus(user)
encoded_password = quote_plus(password)

# URI de connexion à la base de données
uri = f"mongodb+srv://{encoded_user}:{encoded_password}@{cluster}.mongodb.net"

# Connexion au serveur MongoDB
client = MongoClient(uri, server_api=ServerApi('1'), tls=True)
db = client[database_name]
