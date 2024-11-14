import requests

def optionTipFour(id):
    response = requests.delete(f'https://6734e0705995834c8a9132ec.mockapi.io/propina/{id}')
    return response.json()