import time

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Verify spicejet")
@allure.description("Verify user able to enter from details in spicejet")

def test_spicejet_verify():
    driver=webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()

    time.sleep(20)
    fromelement=driver.find_element(By.XPATH,"(//input[@class='css-1cwyjr8 r-homxoj r-ubezar r-10paoce r-13qz1uu'])[1]")
    Toelement=driver.find_element(By.XPATH,"(//input[@class='css-1cwyjr8 r-homxoj r-ubezar r-10paoce r-13qz1uu'])[2]")
    actions=ActionChains(driver=driver)
    actions.move_to_element(to_element=fromelement).click().send_keys_to_element(fromelement,"del").key_down(Keys.TAB).send_keys_to_element(Toelement,"Blr").perform()
    time.sleep(20)


