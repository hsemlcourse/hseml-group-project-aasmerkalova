# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(title="Starbucks Revenue Prediction API")

# Загрузка обученного пайплайна (включает предобработку)
try:
    model = joblib.load('models/best_model.pkl')
    print("Модель успешно загружена")
except Exception as e:
    print(f"Ошибка загрузки модели: {e}")
    model = None

class OrderFeatures(BaseModel):
    order_channel: str
    store_location_type: str
    region: str
    customer_age_group: str
    customer_gender: str
    is_rewards_member: bool
    cart_size: int
    num_customizations: int
    fulfillment_time_min: float
    drink_category: str
    has_food_item: bool
    order_ahead: bool
    customer_satisfaction: int
    day_of_week_num: int
    hour: int
    time_period: str
    month: int
    day_of_month: int
    is_weekend: int

@app.get("/")
def root():
    return {"message": "Starbucks Revenue Prediction API. Use /predict"}

@app.post("/predict")
def predict(features: OrderFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    try:
        # Преобразуем в DataFrame (одна строка)
        input_df = pd.DataFrame([features.dict()])
        prediction = model.predict(input_df)[0]
        return {"predicted_total_spend": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)