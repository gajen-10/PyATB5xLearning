import pytest
import requests

base_url= "https://restful-booker.herokuapp.com"
headers= {"Content-Type" : "application/json"}

def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    payload_auth = {
         "username": "admin",
         "password": "password123"
     }

    response=requests.post(url=full_url,headers=headers,json=payload_auth)
    token=response.json()["token"]

    return token

def get_bookingid():
    base_path="/booking"
    full_url=base_url+base_path

    payload_booking={
        "firstname": "Ravi",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_booking=requests.post(url=full_url,headers=headers,json=payload_booking)
    bookingid=response_booking.json()["bookingid"]

    return bookingid

def test_delete_booking():
    bookingid=get_bookingid()
    token=get_token()
    base_path="/booking/"+str(bookingid)
    full_url=base_url+base_path
    cookie = "token=" + token
    headers_json={"Content-Type":"application-json","cookie":cookie}

    response=requests.delete(url=full_url,headers=headers_json)
    assert response.status_code==201

    response_get=requests.get(url=full_url,headers=headers)
    assert response_get.status_code==404
