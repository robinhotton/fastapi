from fastapi import FastAPI
from app.routers import professeur

app = FastAPI()

app.include_router(professeur.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the DigiSchools API"}