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
    # <a href="https://vwo.com/free-trial/?utm_medium=website&amp;
    # utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">Start a free trial
    # </a>

    # Link text- exact match
    # anchor_tag_webelement=driver.find_element(By.LINK_TEXT,"Start a free trial")
    # anchor_tag_webelement.click()

    # Partial text- contains
    anchor_tag_webelement = driver.find_element(By.PARTIAL_LINK_TEXT, " free trial")
    anchor_tag_webelement.click()


    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    driver.quit()   # close everything
