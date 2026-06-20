from pydantic import BaseModel, Field

class UsedCarCreate(BaseModel):
    fuel_type: int = Field(..., example=1)
    mileage_km: float = Field(..., example=50000)
    year: int = Field(..., example=2020)
    power_hp: float = Field(..., example=150)
    engine_size_cc: float = Field(..., example=1500)
    cylinders: float = Field(..., example=4)
    
class UsedCarPredictionResponse(BaseModel):
    message: str
    price: float
    
class UsedCarResponse(BaseModel):
    id: int = Field(..., example=1)
    fuel_type: int = Field(..., example=1)
    mileage_km: float = Field(..., example=5)
    year: int = Field(..., example=5)
    power_hp: float = Field(..., example=5)
    engine_size_cc: float = Field(..., example=5)
    cylinders: float = Field(..., example=5)
    price: float = Field(..., example=5)