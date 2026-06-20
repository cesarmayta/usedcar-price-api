from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import UsedCar
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
    
@router.post("/",response_model=UsedCarResponse)
def create(data: UsedCarCreate,db: Session = Depends(get_db)):
    price = predict_price(data.fuel_type,
                          data.mileage_km,
                          data.year,
                          data.power_hp,
                          data.engine_size_cc,
                          data.cylinders)
    
    new_data = UsedCar(
        fuel_type = data.fuel_type,
        mileage_km = data.mileage_km,
        year = data.year,
        power_hp = data.power_hp,
        engine_size_cc = data.engine_size_cc,
        cylinders = data.cylinders,
        price = price
    )
    
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data

@router.get("/",response_model=list[UsedCarResponse])
def get_housing(db: Session = Depends(get_db)):
    return db.query(UsedCar).all()