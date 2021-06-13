import requests
import json


def test_post_status():
    
    url = 'http://127.0.0.1:5000/carta'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "cartaId": 1, 
        "remetente": "Marcos Ribeiro",
        "password": "123deoliveira4",
        "conteudo": "Quero um playstation 5"
        }

    resposta = requests.post(url, headers=headers, data=json.dumps(payload))
    assert resposta.status_code == 201 or resposta.status_code == 400

def test_get_status():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5000/carta'

    resposta = requests.get(url, headers=headers)
    assert resposta.status_code == 200

def test_get_by_id_status():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://127.0.0.1:5000/carta/1'

    resposta = requests.get(url, headers=headers)
    assert resposta.status_code == 200

def test_login():
    
    url = 'http://127.0.0.1:5000/carta/login'
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "remetente": "Marcos Ribeiro",
        "password": "123deoliveira4",
    }
    resposta = requests.post(url, headers=headers, data=json.dumps(payload))
    response_content = json.loads(resposta.content.decode('utf-8'))
    return response_content['access_token']

def test_put_status():
    
    url = 'http://127.0.0.1:5000/carta/1'
    headers = {
        'Content-Type': 'application/json',
        'Authorization':'Bearer ' + test_login()
    }
    payload = {
        "remetente": "Marcos Cesar Ribeiro",
        "password": "123deoliveira4",
        "conteudo": "Quero um playstation 5"
    }
    resposta = requests.put(url, headers=headers, data=json.dumps(payload))
    assert resposta.status_code == 200 or resposta.status_code == 201

def test_delete_status():

    headers = {
        'Content-Type': 'application/json',
        'Authorization':'Bearer ' + test_login()
    }
    url = 'http://127.0.0.1:5000/carta/1'

    resposta = requests.delete(url, headers=headers)
    assert resposta.status_code == 200