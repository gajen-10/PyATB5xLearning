import time

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("Window Handle")
@allure.description("Verify switching between windows")
def test_window_handle():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")

    time.sleep(10)

    parent_window=driver.current_window_handle
    print(parent_window)

    new_window=driver.find_element(By.XPATH,"//a[contains(text(),'Click Here')]")
    new_window.click()

    window_handle=driver.window_handles
    print(window_handle)

    for handle in window_handle:
        driver.switch_to.window(handle)
        if "New window" in driver.page_source:
            #assert True,"Testcase Passed"
            print("Testcase Passed")

    time.sleep(5)
