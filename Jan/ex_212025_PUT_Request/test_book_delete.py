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

def create_booking():
    base_path="/booking"
    full_url=base_url+base_path

    payload_json={
        "firstname": "Roger",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_create=requests.post(url=full_url,headers=headers,json=payload_json)

    bookingid=response_create.json()["bookingid"]

    return bookingid

def test_delete():
    bookingid=create_booking()
    token=get_token()

    base_path="/booking/"+str(bookingid)
    cookie="token="+token
    full_url=base_url+base_path
    headers={"Content-Type":"application/json","cookie":cookie}

    response_delete=requests.delete(url=full_url,headers=headers)

    assert response_delete.status_code==201