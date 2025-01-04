import allure
import pytest
import requests

@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This testcase check Booking and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url=URL)
    print(response_data.text)
    assert response_data.status_code==200


@allure.title("Verify the GET Request of Restful Booker with invlaid ID")
@allure.description("This testcase check Booking and verify the response")
@pytest.mark.positive
def test_get_request_negative():
    URL = "https://restful-booker.herokuapp.com/booking/-1"
    response_data=requests.get(url=URL)
    print(response_data.text)
    assert response_data.status_code==404