from fastapi import FastAPI
from api.schema import HouseRequest

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API working"}

@app.post("/predict")
def predict(data: HouseRequest):
    return {"prediction": "dummy"}