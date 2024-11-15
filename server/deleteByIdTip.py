import requests

def optionTipFour(id):
    response = requests.delete(f'https://67373485aafa2ef22233052c.mockapi.io/tip/{id}')
    return response.json()