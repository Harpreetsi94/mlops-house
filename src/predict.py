import joblib
import numpy as np

MODEL_PATH = "../models/model.pkl"

model = joblib.load(MODEL_PATH)

def predict(size):

    prediction = model.predict(np.array([[size]]))

    return prediction[0]