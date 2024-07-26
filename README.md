# FastAPI with MongoDB (PyMongo) Project

## Description

Ce projet est une API web développée avec [FastAPI](https://fastapi.tiangolo.com/) et connectée à une base de données MongoDB via [PyMongo](https://pymongo.readthedocs.io/). Il s'agit d'une application CRUD (Create, Read, Update, Delete) simple pour gérer les informations des professeurs.

## Architecture du Projet

Le projet est organisé selon l'architecture suivante :

```sh
fastapi/
│
├── app/
│   │
│   ├── crud/
│   │   └── professeur.py    # Logique de base de données pour les opérations CRUD
│   │
│   ├── routes/
│   │   └── professeur.py    # Routes API pour les opérations sur les professeurs
│   │
│   ├── schema/
│   │   └── professeur.py    # Modèles de données (schemas) pour les professeurs
│   │
│   ├── main.py              # Point d'entrée principal de l'application
│   └── database.py          # Configuration de la connexion à MongoDB
│
├── .env                 # Variables d'environnement
├── requirements.txt     # Dépendances Python
├── run.sh               # Script pour lancer le serveur sous Unix/Linux
├── run.bat              # Script pour lancer le serveur sous Windows
├── .gitignore           # Fichiers à ignorer par Git
└── .venv                # Environnement virtuel Python
```

## Fonctionnalités

- **Créer** un professeur.
- **Lire** les informations des professeurs ou spécifiquement un selon son _id.
- **Mettre à jour** les informations d'un professeur selon son _id.
- **Supprimer** un professeur de la base de données selon son _id.

## Prérequis

- `Python` 3.8 ou supérieur
- `MongoDB`
- `pip` pour la gestion des paquets

## Installation

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/robinhotton/fastapi.git
   cd fastapi
   ```

2. **Créer et activer un environnement virtuel**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows utilisez .venv\Scripts\activate
   ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données**

   Assurez-vous que MongoDB est installé et en cours d'exécution. Créez un fichier `.env` dans le répertoire racine du projet et configurez votre connexion MongoDB avec vos informations avec la structure du .env.example :

## Utilisation

### Démarrer le serveur

#### Sur Unix/Linux

Utilisez le script `run.sh` pour lancer sur le port 8000 par défaut, ou le port de votre choix en ajoutant un argument :

```bash
./run.sh # Port par défaut 8000
./run.sh 8080 # Port spécifique 8080
```

#### Sur Windows

Utilisez le script `run.bat` pour lancer sur le port 8000 par défaut, ou le port de votre choix en ajoutant un argument :

```bash
.\run.bat # Port par défaut 8000
.\run.bat 8080 # Port spécifique 8080
```

Vous pouvez accéder à l'interface interactive Swagger UI à `http://127.0.0.1:8000/docs`, avec le port spécifié à la place du 8000 si vous avez choisi un autre port.

### Tester l'API

Vous pouvez utiliser des outils comme [Postman](https://www.postman.com/) ou [cURL](https://curl.se/) pour interagir avec l'API. Pour notre part Swagger enverra des requêtes cURL. Voici quelques exemples d'utilisation de cURL :

- **Créer un professeur :**

  ```bash
  curl -X POST "http://127.0.0.1:8000/professeurs" -H "Content-Type: application/json" -d '{"nom": "Dupont", "matiere": "Mathématiques"}'
  ```

- **Lire les informations d'un professeur :**

  ```bash
  curl -X GET "http://127.0.0.1:8000/professeurs/{id}"
  ```

- **Mettre à jour un professeur :**

  ```bash
  curl -X PUT "http://127.0.0.1:8000/professeurs/{id}" -H "Content-Type: application/json" -d '{"nom": "Durand", "matiere": "Physique"}'
  ```

- **Supprimer un professeur :**

  ```bash
  curl -X DELETE "http://127.0.0.1:8000/professeurs/{id}"
  ```

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [PyMongo](https://pymongo.readthedocs.io/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [cURL](https://curl.se/)
- [Postman](https://www.postman.com/)