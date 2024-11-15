import requests

def optionTipFive(id, update):
    response = requests.put(f'https://67373485aafa2ef22233052c.mockapi.io/tip/{id}', json=update)
    return response.json()