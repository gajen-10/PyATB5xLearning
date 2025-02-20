import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("App.VWO.com Implicit wait")
@allure.description("Verify app.vwo.com is loaded with waits")
def test_negative_appVWO_com():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    driver.implicitly_wait(5)

    mailid=driver.find_element(By.ID,"login-username")
    mailid.send_keys("abc@gmail.com")