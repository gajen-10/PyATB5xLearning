import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type" : "application/json"}
def get_token():
    base_path="/auth"

    full_url=base_url+base_path
    payload={
        "username": "admin",
        "password": "password123"
    }

    response=requests.post(url=full_url,headers=headers,json=payload)
    token = response.json()["token"]
    return token

def get_booking_id():
    base_path="/booking"

    full_url = base_url+base_path
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response=requests.post(url=full_url,headers=headers,json=payload)
    booking_id = response.json()["bookingid"]

    return booking_id

def test_patch_name():
    bookingid = get_booking_id()
    token = get_token()

    base_path = "/booking/" + str(bookingid)
    cookie = "token=" + token

    full_url=base_url+base_path
    headers = {
        "Content-Type" : "application/json", "cookie":cookie
    }

    payload = {
        "firstname": "Gajendran",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_json = requests.put(url=full_url,headers=headers,json=payload)
    assert response_json.json()["firstname"] == "Gajendran"