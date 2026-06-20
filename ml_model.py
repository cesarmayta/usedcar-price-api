import joblib
import numpy as np

# Load the best model
model = joblib.load('./model/model.pkl')

# Load the scalers
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')


def predict_price(fuel_type:int,
                  mileage_km: float,
                  year: int,
                  power_hp: float,
                  engine_size_cc: float,
                  cylinders: float)-> float:
    new_car_features = [
        fuel_type,  # Fuel_Type (e.g., 1.0 for 'Other', 0.0 for 'Gasoline')
        mileage_km, # Mileage_km
        year,  # Year
        power_hp,   # Power_hp
        engine_size_cc,  # Engine_Size_cc
        cylinders      # Cylinders
    ]
    new_car_data = np.array(new_car_features).reshape(1, -1)
    new_car_scaled = scaler_X.transform(new_car_data)
    predicted_price_scaled = model.predict(new_car_scaled)
    predicted_price = scaler_y.inverse_transform(predicted_price_scaled.reshape(-1, 1))
    price = round(float(predicted_price[0][0]), 2)
    return price