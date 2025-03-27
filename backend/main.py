from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/data")
def get_data():
    with open("./data.json", "r") as file:
        data = json.load(file)
    return data