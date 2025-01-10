import allure
import pytest
import requests


# Create Token - POST

base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type" : "application/json"}
def get_token():
   base_path = "/auth"
   full_url = base_url + base_path
   json_payload_auth = {
       "username": "admin",
       "password": "password123"
   }

   response_data = requests.post(url=full_url,headers=headers,json=json_payload_auth)

   assert response_data.status_code == 200
   response_json = response_data.json()
   token = response_json["token"]
   print(token)
   assert  type(token) == str
   assert  len(token) > 0

   return token

def get_booking_id():

   base_path = "/booking"
   full_url= base_url + base_path
   payload_json={

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
   response_data= requests.post(url=full_url,headers=headers,json=payload_json)
   response_json = response_data.json()
   booking_id = response_json["bookingid"]

   return booking_id

def test_put_request():
   token=get_token()
   booking_id=get_booking_id()
   print(token)
   print(booking_id)

   base_path = "/booking/" + str(booking_id)
   full_url_put=base_url+base_path
   cookie = "token=" + token

   headers={
       "Content-Type": "application/json",
       "Cookie": cookie

   }

   json_payload = {

            "firstname": "Pramod",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"

    }

   response = requests.put(url=full_url_put,headers=headers,json=json_payload)
   assert response.status_code == 200
   assert response.json()["firstname"] == "Pramod"


def test_delete_request():
    base_url="https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    cookie= "token=" + get_token()
    delete_url= base_url + str(booking_id)

    headers={
        "Content-Type": "application/json",
            "Cookie": cookie
    }
    response= requests.delete(url=delete_url,headers=headers)
    assert response.status_code == 201



