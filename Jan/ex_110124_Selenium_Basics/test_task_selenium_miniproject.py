import pytest
import allure
import time
from selenium import webdriver


@allure.title("Open the Espo CRM")
@pytest.mark.regression
@allure.title("Verify the title and current url of Espo CRM as expected")


def test_open_espo():
    driver=webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(10)
    print(driver.title)
    assert driver.title=="EspoCRM Demo"
    assert driver.current_url == "https://demo.us.espocrm.com/"





