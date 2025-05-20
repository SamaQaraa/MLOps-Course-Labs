from fastapi import FastAPI
import joblib
import pickle
import pandas as pd
from pydantic import BaseModel , Field
import logging

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model
with open("transformer.pkl", "rb") as f:
    transformer = pickle.load(f)
model = joblib.load("models/GBOOST_model.pkl")


class InputData(BaseModel):
    CreditScore: int = Field(..., example=650)
    Geography: str = Field(..., example="France")
    Gender: str = Field(..., example="Female")
    Age: int = Field(..., example=40)
    Tenure: int = Field(..., example=5)
    Balance: float = Field(..., example=50000.0)
    NumOfProducts: int = Field(..., example=2)
    HasCrCard: int = Field(..., example=1)
    IsActiveMember: int = Field(..., example=1)
    EstimatedSalary: float = Field(..., example=60000.0)


app = FastAPI()

@app.get("/")
def home():
    logger.info("Home endpoint hit")
    return {"message": "Welcome to the Prediction API"}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "OK"}

@app.post("/predict")
def predict(data: InputData):
    logger.info(f"Received prediction request: {data}")
    input_dict = data.dict()
    X_df = pd.DataFrame([input_dict])
    transformed = transformer.transform(X_df)
    prediction = model.predict(transformed)[0]
    logger.info(f"Prediction: {prediction}")
    return {"prediction": int(prediction)}





# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# To run the server, use the command:
#uvicorn main:app --reload

