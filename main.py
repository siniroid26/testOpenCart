import requests

url = 'https://test.aspor.ua/index.php?route=api/login'

headers = {
    'Content-Type': 'application/json',
    'X-Oc-Image-Dimension': '64x64'
}

data = {
    'username': 'aspor32',
    'key': 'VqWUxWnOH223DPB1TR1sqnj6wLJofsHQvxjYmr8lJ7FS3torc51Nj0b2msAK3doaNbCXB8GQtuK2Fr31kbVX7BBtkyC68EoSzCb78Z80jZkABuKHAUtHKNL44yFSUwSmRuzYKG4K8pCFXzStRyuHxTteaw4ggpqUcPEOXjNasNUqp6NxLoTsoNFsfKkc3BOKVsRO5Ip8hNPUFquklnCZrDMKxFyKSWVRSBU48Q0PZ7dB7OnzCzYGN82AuBZOcDsq'
}

response = requests.post(url, headers=headers, json=data)
print(response)

if response.status_code == 200:
    token = response.json()['token']
    print(f'Успешная аутентификация. Токен: {token}')
else:
    print(f'Ошибка при аутентификации: {response.status_code}')
