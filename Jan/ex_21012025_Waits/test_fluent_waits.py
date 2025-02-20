import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("App.VWO.com Implicit wait")
@allure.description("Verify app.vwo.com is loaded with waits")
def test_negative_appVWO_com():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    #driver.implicitly_wait(5)

    mailid=driver.find_element(By.ID,"login-username")
    mailid.send_keys("abc@gmail.com")

    password=driver.find_element(By.ID,"password")
    password.send_keys("password@1234")

    submit_btn_webelement=driver.find_element(By.ID,"js-login-btn")
    submit_btn_webelement.click()
    # Wait for the error message

    # A Condition to check the element
    # error_msg_element - comes after 2-4 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion
    # when  this -> then do this

    # Smart Logic to wait for the element
    # Condition based Logic

    # Verify that message is visible.
    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match</div>

    # time.sleep(5) # Python Int to wait for 5 seconds without any condition.

    WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located(By.CLASS_NAME,"notification-box-description"))

    err_mess_webelement=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(err_mess_webelement.text)
    assert err_mess_webelement.text == "Your email, password, IP address or location did not match"
