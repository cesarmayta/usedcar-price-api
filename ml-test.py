import joblib
import numpy as np

# Load the best model
model = joblib.load('./model/model.pkl')

# Load the scalers
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')

print("Model and scalers loaded successfully!")

new_car_features = [
    1.0,  # Fuel_Type (e.g., 1.0 for 'Other', 0.0 for 'Gasoline')
    50000, # Mileage_km
    2020,  # Year
    150,   # Power_hp
    1500,  # Engine_Size_cc
    4      # Cylinders
]

# Convert to numpy array and reshape for the scaler
new_car_data = np.array(new_car_features).reshape(1, -1)

# Scale the new data using the pre-fitted scaler_X
new_car_scaled = scaler_X.transform(new_car_data)

# Make a prediction with the loaded model
predicted_price_scaled = model.predict(new_car_scaled)

# Inverse transform the predicted price to the original scale
predicted_price = scaler_y.inverse_transform(predicted_price_scaled.reshape(-1, 1))

print(f"Predicted price for the new car: ${predicted_price[0][0]:,.2f}")