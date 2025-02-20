import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Modal")
@allure.description("Verify moda;")
def test_modal():
    driver=webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()


    WebDriverWait(driver=driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//section[@data-cy='CommonModal_2']")))

    modal=driver.find_element(By.XPATH,"//span[@data-cy='closeModal']")
    modal.click()

def test_modal_value():
    driver=webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Enter Mobile Number']")))

    modal_input=driver.find_element(By.XPATH,"//input[@placeholder='Enter Mobile Number']")
    modal_input.send_keys("999782321")

    cont_btn=driver.find_element(By.XPATH,"//button[@data-cy='continueBtn']")
    cont_btn.click()