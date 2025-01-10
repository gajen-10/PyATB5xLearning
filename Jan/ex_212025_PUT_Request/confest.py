import pytest
import requests
from dotenv import load_dotenv
import os

@pytest.fixture()
def create_token():
    load_dotenv()
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")

    print(username)
    print(password)
    baseurl="https://restful-booker.herokuapp.com"
    basepath="/auth"
    full_url=baseurl+basepath
    headers = {"Content-Type": "application/json"}
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }

    response=requests.post(url=full_url,headers=headers,json=json_payload_auth)
    token=response.json()["token"]

    print(token)
    return token
@pytest.fixture()
def create_bookingid():
    baseurl="https://restful-booker.herokuapp.com"
    basepath="/booking"

    full_url=baseurl+basepath
    headers={
        "Content-Type":"application/json"}

    payload={
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

    booking_ID=response.json()["bookingid"]
    return booking_ID

@pytest.fixture()
def read_csv_file_data():
    pass

@pytest.fixture()
def read_mysql_file_database():
    pass

@pytest.fixture()
def read_url_test_dataexcel():
    pass

@pytest.fixture()
def launch_browser():
    print("Launching Browser!! chrome")
    return "chrome"

@pytest.fixture()
def closing_browser():
    print("closing chrome browser!!")
    return "closed"