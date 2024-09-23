from fastapi import FastAPI
import numpy as np
from .schema import InputData, PredictionResponse



app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(data: InputData):
    X = np.array([[data.first_bit.value, data.second_bit.value]])

    prediction = [data.first_bit.value + data.second_bit.value]
    return {"prediction": prediction[0]}

