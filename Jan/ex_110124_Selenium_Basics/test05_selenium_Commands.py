import pytest
import allure

from selenium import webdriver


@allure.title("Open the app.vwo.com")
@pytest.mark.regression

@allure.title("Verify the title of vwo.com is expected")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"



