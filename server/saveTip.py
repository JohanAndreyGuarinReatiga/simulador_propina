import requests
def saveTip(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://67373485aafa2ef22233052c.mockapi.io/tip', headers=headers, json=data)
    return response.json()