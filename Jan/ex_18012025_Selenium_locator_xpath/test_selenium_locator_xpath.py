from selenium import webdriver

import allure
import pytest
import time

from selenium.webdriver.common.by import By


def test_katalon_driver():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment= driver.find_element(By.XPATH,"//a[text()='Make Appointment']")
    make_appointment.click()

    # text() -> Exact Match

    # Partial Text() - contains()
    # //a[contains(text(),'Make Appointment')]
    # //a[contains(text(),'Appointment')]
    # //a[contains(text(),'Make')]
    # //a[contains(text(),'Ma')]
    # //a[contains(text(),'App')] - This may fail if there 1 or more a tag with App.
    # <a rel="https:/google.com"/>

    # //a[starts-with(text(),'Make')]
    
    time.sleep(5)
    driver.quit()