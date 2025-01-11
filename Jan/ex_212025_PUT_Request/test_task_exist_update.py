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

def get_bookingid():
    base_path="/booking"

    full_url=base_url+base_path

    response=requests.get(url=full_url,headers=headers)
    booking_id=response.json()[0]["bookingid"]
    print(booking_id)
    return booking_id


def test_update_exisiting():
    token=get_token()
    booking_id=get_bookingid()

    base_path="/booking/"+str(booking_id)
    cookie="token="+token
    full_url=base_url+base_path
    headers_exist={"Content-Type":"application/json","cookie":cookie}

    payload_exist={
        "firstname": "Raj",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response=requests.put(url=full_url,headers=headers_exist,json=payload_exist)

    assert response.json()["firstname"] == "Raj"

    response_get=requests.get(url=full_url,headers=headers)
    assert response_get.json()["firstname"] == "Raj"
