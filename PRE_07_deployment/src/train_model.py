import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Cargar los datos desde la carpeta data
# Ajusta la ruta si tu archivo house_data.csv está en otra ubicación
data_path = os.path.join("PRE_07_deployment", "data", "house_data.csv")
df = pd.read_csv(data_path)

# 2. Definir las variables explicativas (X) y la variable objetivo (y)
feature_cols = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "condition",
]

features = df[feature_cols]
target = df["price"]

# 3. Crear y entrenar el modelo
estimator = LinearRegression()
estimator.fit(features, target)

# 4. Guardar el modelo entrenado en la carpeta src o output
output_dir = os.path.join("PRE_07_deployment", "src")
os.makedirs(output_dir, exist_ok=True)

model_path = os.path.join(output_dir, "model.pkl")
joblib.dump(estimator, model_path)

print(f"Modelo entrenado y guardado exitosamente en: {model_path}")