import requests

def make_request():
    url = 'http://127.0.0.1:5000/predict'
    
    # Datos de la propiedad que le enviaremos al servidor
    data = {
        "sqft_living": "1800",
        "sqft_lot": "2200",
        "floors": "1",
        "waterfront": "1",
        "condition": "3"
    }
    
    # Enviar la petición POST con los datos JSON
    response = requests.post(url, json=data, timeout=5)
    
    # Imprimir la respuesta del servidor
    print("Código de estado:", response.status_code)
    print("Respuesta del servidor:", response.text)

if __name__ == '__main__':
    make_request()