import allure
import pytest
import requests


@allure.title("TC#1 Create Booking ")
@allure.description("Verify whether the booking created or not")
@pytest.mark.curd
def test_create_booking():
    base_url= "https://restful-booker.herokuapp.com"
    base_path= "/booking"
    header={"Content-Type" : "application/json"}
    full_url = base_url + base_path

    payload= {

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

    response_data=requests.post(url=full_url,headers=header,json=payload)

    assert response_data.status_code == 200

    response_json=response_data.json()

    firstname = response_json["booking"]["firstname"]

    assert firstname == "Jim"


allure.title("TC#2 Get the booking ID")
allure.description("Verify whether we can able to fetch booking id")
pytest.mark.curd
def test_get_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "booking/1"
    full_url = base_url + base_path


    response_data = requests.get("https://restful-booker.herokuapp.com/booking/1")
    assert response_data.status_code==200

    print(response_data.text)