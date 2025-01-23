import pytest
import allure

from selenium import webdriver


@allure.title("Open the app.vwo.com")
@pytest.mark.regression

def test_vwo_login_selenium_3():
    driver_path = ''
    driver=webdriver.EdgeService(executable_path=driver_path)
    driver.get("https/:vwo.app.com")



