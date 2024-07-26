#!/bin/bash

# Définir un port par défaut
DEFAULT_PORT=8000

pip install -r requirements.txt

# Vérifie si un argument est fourni
if [ -z "$1" ]; then
    uvicorn app.main:app --port $DEFAULT_PORT --reload
else
    uvicorn app.main:app --port $1 --reload
fi
