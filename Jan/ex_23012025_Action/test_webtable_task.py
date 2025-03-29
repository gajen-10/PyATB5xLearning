import time

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



@allure.title("Delete terminated")
@allure.description("Delete first terminated person")

def test_webtable():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(10)

    usrname=driver.find_element(By.XPATH,"//input[@name='username']")
    passwrd=driver.find_element(By.XPATH,"//input[@name='password']")

    usrname.send_keys("admin")
    passwrd.send_keys("Hacker@4321")

    submit=driver.find_element(By.XPATH,"//button[@type='submit']")

    submit.click()

    time.sleep(5)

    delete_btn=driver.find_element(By.XPATH,"(//div[contains(text(),'Terminated')])[1]/following::button[1]")
    delete_btn.click()
    time.sleep(5)