import pytest
import requests

base_url="https://restful-booker.herokuapp.com"
headers= {"Content-Type" : "application/json"}
def get_token():
    base_path="/auth"

    full_url=base_url+base_path
    payload={
        "username": "admin",
        "password": "password123"
    }

    response=requests.post(url=full_url,headers=headers,json=payload)
    token=response.json()["token"]

    return token

def test_create_booking():
    base_path="/booking"
    full_url=base_url+base_path

    payload_json={
        "firstname": "Roger",
        "lastname": "Brown",
        "totalprice": 111,
        "": True,
        "b":""
    }

    response_create=requests.post(url=full_url,headers=headers,json=payload_json)

    assert response_create.status_code==500