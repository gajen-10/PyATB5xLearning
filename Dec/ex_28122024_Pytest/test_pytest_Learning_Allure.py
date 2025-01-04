import allure
import pytest


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This testcase check or the positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("test 1")
    assert 1-1 == 2


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This testcase check or the negative create booking")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("test 2")
    assert 1+1 == 2


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This testcase check or the negative create booking")
@pytest.mark.negative
def test_create_booking_negative_2c():
    print("test 2")
    assert 1+1 == 2

