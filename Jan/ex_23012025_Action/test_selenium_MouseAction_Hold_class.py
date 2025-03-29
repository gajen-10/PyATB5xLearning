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


@allure.title("Selenium Mouse Action Click and hold Class")
@allure.description("Verify Mouse Action Click and Hold performed")
def test_action_element():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    drag_ele=driver.find_element(By.ID,"draggable")

    Action=ActionChains(driver)
    Action.click_and_hold(on_element=drag_ele).perform()

    time.sleep(20)
    driver.quit()