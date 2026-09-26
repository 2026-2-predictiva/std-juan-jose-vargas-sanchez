from flask import Flask, request, jsonify

app = Flask(__name__)

# En un caso real, aquí cargarías un modelo previamente guardado (ej. con joblib o pickle)
# model = joblib.load('modelo_viviendas.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos JSON enviados por el cliente
    data = request.get_json()
    
    # Extraer las variables del JSON
    sqft_living = float(data.get('sqft_living', 0))
    floors = float(data.get('floors', 1))
    condition = float(data.get('condition', 3))
    
    # Ejemplo de "modelo" ficticio: cálculo simple para simular la predicción
    # (En la práctica usarías: prediccion = model.predict([features]))
    predicted_price = (sqft_living * 500) + (floors * 10000) + (condition * 5000)
    
    # Responder con la predicción en formato JSON
    return jsonify({
        'status': 'success',
        'predicted_price': predicted_price
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)