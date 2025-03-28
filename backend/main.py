from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Orígenes permitidos desde una variable de entorno o configuracion
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Lista de dominios permitidos
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    with open("./data.json", "r") as file:
        data = json.load(file)
    return data