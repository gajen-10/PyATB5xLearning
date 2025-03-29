import time

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Selenium Action Class")
@allure.description("Verify Action performed")
def test_action_element():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")

    Actions=ActionChains(driver=driver)
    Actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"the testing academy").key_up(Keys.SHIFT).perform()
    time.sleep(20)
    driver.quit()