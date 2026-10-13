from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel,Field

app=FastAPI(title="IRIS MODEL API ENDPOINT")
model_path=Path("models/iris_model.joblib")
model=joblib.load(model_path)

class IrisRequest(BaseModel):
    sepal_length: float = Field(..., example=5.1, description="Sepal length in cm")
    sepal_width: float = Field(..., example=3.5, description="Sepal width in cm")
    petal_length: float = Field(..., example=1.4, description="Petal length in cm")
    petal_width: float = Field(..., example=0.2, description="Petal width in cm")

@app.get("/health")
def  health_check():
    return {"status":"healthy"}

