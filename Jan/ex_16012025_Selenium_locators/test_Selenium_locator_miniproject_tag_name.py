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

    all_links_page=driver.find_elements(By.TAG_NAME,"a")
    print(len(all_links_page))

    for i in all_links_page:
        print(i.text)
        if "Start a free trial" in i.text:
            i.click()


    # assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    driver.quit()   # close everything
