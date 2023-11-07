from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Ваши данные для API
api_name = 'aspor32'
api_key = 'VqWUxWnOH223DPB1TR1sqnj6wLJofsHQvxjYmr8lJ7FS3torc51Nj0b2msAK3doaNbCXB8GQtuK2Fr31kbVX7BBtkyC68EoSzCb78Z80jZkABuKHAUtHKNL44yFSUwSmRuzYKG4K8pCFXzStRyuHxTteaw4ggpqUcPEOXjNasNUqp6NxLoTsoNFsfKkc3BOKVsRO5Ip8hNPUFquklnCZrDMKxFyKSWVRSBU48Q0PZ7dB7OnzCzYGN82AuBZOcDsq'
# URL API
url = 'https://test.aspor.ua'

@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get(f'{url}/api/products', headers={'api_name': api_name, 'api_key': api_key})
    products = response.json()
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
