import allure
import pytest


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This testcase check or the positive create booking")
@pytest.mark.smoke
def test_basic_math():
    print("test 1")
    assert 1-1 == 2


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This testcase check or the negative create booking")
@pytest.mark.Regression
def test_sub1():
    print("test 2")
    assert 1+1 == 2


@allure.title("Verify that create booking, with valid data is working")
@allure.description("This testcase check or the negative create booking")
@pytest.mark.smoke
def test_add():
    print("test 2")
    assert 1+1 == 2

@pytest.mark.skip(reason="not working, Skip it!!")
def test_sub2():
    assert 0-0!=0

