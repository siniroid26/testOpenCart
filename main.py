import requests
def get_external_ip():
    response = requests.get("http://ipinfo.io/json")
    data = response.json()
    return data.get('ip')

external_ip = get_external_ip()
print(f"Ваш внешний IP-адрес: {external_ip}")
import json

# Ваши данные для API
api_name = 'aspor32'
api_key = 'VqWUxWnOH223DPB1TR1sqnj6wLJofsHQvxjYmr8lJ7FS3torc51Nj0b2msAK3doaNbCXB8GQtuK2Fr31kbVX7BBtkyC68EoSzCb78Z80jZkABuKHAUtHKNL44yFSUwSmRuzYKG4K8pCFXzStRyuHxTteaw4ggpqUcPEOXjNasNUqp6NxLoTsoNFsfKkc3BOKVsRO5Ip8hNPUFquklnCZrDMKxFyKSWVRSBU48Q0PZ7dB7OnzCzYGN82AuBZOcDsq'
# URL API
url = 'https://test.aspor.ua/api/rest/categories'

# Заголовки для запроса
headers = {
    'Content-Type': 'application/json',
    'Api-Name': api_name,
    'Api-Key': api_key
}

# Отправляем запрос
response = requests.get(url, headers=headers)

# Проверяем статус ответа
if response.status_code == 200:
    # Преобразуем ответ в JSON
    data = response.json()

    # Выводим категории товаров
    for category in data['data']:
        print(category['name'])
else:
    print(f'Ошибка подключения: {response.status_code}')
