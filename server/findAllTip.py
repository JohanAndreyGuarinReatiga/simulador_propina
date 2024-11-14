import requests

def optionTipOne():
    response = requests.get('https://6734e0705995834c8a9132ec.mockapi.io/propina')
    return response.json()

