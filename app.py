from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/predict")
def predict(x: float):
    prediction = model.predict(np.array([[x]]))
    return {"prediction": prediction.tolist()}