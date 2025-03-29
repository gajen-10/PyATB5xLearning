import time

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Verify Makemytrip website")
@allure.description("Verify Makemytrip website")
def test_makemytrip():
    driver=webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

    Close_Modal=driver.find_element(By.XPATH,"//span[@data-cy='closeModal']")
    Close_Modal.click()

    time.sleep(10)

    fromcity=driver.find_element(By.ID,"fromCity")

    actions=ActionChains(driver=driver)
    actions.move_to_element(fromcity).click().send_keys_to_element(fromcity,"del").perform()
    time.sleep(3)

    actions.move_to_element(fromcity).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()


    time.sleep(10)


