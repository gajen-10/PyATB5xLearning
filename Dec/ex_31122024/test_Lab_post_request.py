import allure
import pytest
import requests


@allure.title("TC#1- Create Booking CRUD Positive")
@allure.description("Verify the create booking")
@pytest.mark.CURD
def test_create_booking_positive():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"

    full_url=base_url+base_path

    headers={
        "Content-Type" : "application/json"
    }
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

    response_data= requests.post(url=full_url,headers=headers,json=payload)

    assert response_data.status_code == 200

    Response_Json=response_data.json()

    Booking_Id = Response_Json["bookingid"]
    print(Booking_Id)

    assert Booking_Id is not None
    assert Booking_Id > 0
    assert type(Booking_Id) == int

    firstname=Response_Json["booking"]["firstname"]
    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = Response_Json["booking"]["lastname"]
    totalprice = Response_Json["booking"]["totalprice"]
    depositpaid = Response_Json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin= Response_Json["booking"]["bookingdates"]["checkin"]
    checkout = Response_Json["booking"]["bookingdates"]["checkout"]

    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    time = response_data.elapsed.total_seconds()
    assert time < 3



@allure.title("TC#2 Create booking CURD Negative ")
@allure.description("Verify that invalid payload Booking is not created !")
@pytest.mark.CURD
def test_create_booking_negative_tc():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"

    URL = base_url + base_path
    headers = {"Content-Type" : "application/json"}

    Payload = {}

    response_data = requests.post(url=URL,headers=headers,json=Payload)

    assert response_data.status_code == 500
    assert response_data.text == "Internal Server Error"

