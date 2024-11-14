import requests

def optionTipThree(id):
    response = requests.get(f'https://6734e0705995834c8a9132ec.mockapi.io/propina/{id}')
    return response.json()