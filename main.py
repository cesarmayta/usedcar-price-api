from fastapi import FastAPI
from database import engine
from models import Base
from routers import usedcars

app = FastAPI(
    title="UserCars API ",
    description="API para predicción de precios de autos usados",
    version="1.0.0"
)

app.include_router(usedcars.router)

@app.get("/")
def index():
    return {
        "title": "USED CARS API VERSION 1.0",
        "message": "Bienvenido a mi API"
    }
    
#Base.metadata.create_all(engine)