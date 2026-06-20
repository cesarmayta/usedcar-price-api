from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import UsedCars
from ml_model import predict_price

from schemas import (
    UsedCarCreate,
    UsedCarPredictionResponse,
    UsedCarResponse
)

router = APIRouter(
    prefix="/usedcar",
    tags=["usedcar"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/price",response_model=UsedCarPredictionResponse)
def housing_price(data: UsedCarCreate):
    price = predict_price(data.fuel_type,
                          data.mileage_km,
                          data.year,
                          data.power_hp,
                          data.engine_size_cc,
                          data.cylinders)

    return {
        "message": "precio predicho",
        "price": price
    }