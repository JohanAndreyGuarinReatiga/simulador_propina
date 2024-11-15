import requests

def optionTipThree(id):
    response = requests.get(f'https://67373485aafa2ef22233052c.mockapi.io/tip/{id}')
    return response.json()