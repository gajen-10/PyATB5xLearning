from selenium import webdriver

import allure
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os



@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with invalid creds.")
@pytest.mark.negativevwologin
def test_katalon_driver():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("window-size=900,600")
    # chrome_options.add_argument("--headless")

    load_dotenv()
    driver=webdriver.Chrome()
    driver.get(os.getenv("URL"))
    # 1- Find the email id textbox and enter wrong username
    # <input type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi">


    email_webelement=driver.find_element(By.ID,"login-username")
    email_webelement.send_keys(os.getenv("Invalid_USERNAME"))

    # <input type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe">

    password_webelement=driver.find_element(By.ID,"login-password")
    password_webelement.send_keys(os.getenv("Invalid_PASSWORD"))

    # <button type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">
    #

    submit_btn_webelement=driver.find_element(By.ID,"js-login-btn")
    submit_btn_webelement.click()

    #Wit for sometime
    time.sleep(5)

    # <div class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password, IP address or location did not match</div>

    error_message_webelement=driver.find_element(By.ID,"js-notification-box-msg" )
    print(error_message_webelement.text)

    assert error_message_webelement.text == os.getenv("error_message_expected")
    driver.quit()   # close everything
