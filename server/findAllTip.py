import requests

def optionTipOne():
    response = requests.get('https://67373485aafa2ef22233052c.mockapi.io/tip')
    return response.json()

