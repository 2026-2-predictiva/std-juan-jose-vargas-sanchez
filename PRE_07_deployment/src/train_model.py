import os
import pickle
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

def train():
    # Cargar datos de entrenamiento
    data = fetch_california_housing(as_frame=True)
    X, y = data.data, data.target

    # Entrenar modelo
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X, y)

    # Asegurar la creación de la carpeta submission y guardar el modelo pkl
    os.makedirs("PRE_07_deployment/submission", exist_ok=True)
    model_path = "PRE_07_deployment/submission/house_predictor.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    
    print(f"Modelo creado exitosamente en: {model_path}")

if __name__ == "__main__":
    train()