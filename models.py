from sqlalchemy import Column, Integer, Float, String
from database import Base

class UsedCar(Base):
    __tablename__ = "usedcars"
    
    id = Column(Integer, primary_key=True, index=True)
    fuel_type = Column(Integer, nullable=False)
    mileage_km = Column(Float, nullable=False)
    year = Column(Float, nullable=False)
    power_hp = Column(Float, nullable=False)
    engine_size_cc = Column(Float, nullable=False)
    cylinders = Column(Float, nullable=False)
    price = Column(Float, nullable=True)