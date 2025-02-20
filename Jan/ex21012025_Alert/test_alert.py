import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Alerts")
@allure.description("Verify alerts")
def test_negative_appVWO_com():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_prompt=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    element_prompt.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.accept()
    result_text = driver.find_element(By.ID,"result").text
    assert result_text=="You successfully clicked an alert"


def test_confirmation_alert():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_conpromp=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    element_conpromp.click()

    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.dismiss()
    Result_txt=driver.find_element(By.ID,"result").text
    assert Result_txt=="You clicked: Cancel"

def test_prompt_alert():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_promp=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    element_promp.click()

    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.send_keys("I am clicked")
    alert.accept()


    res_txt=driver.find_element(By.ID,"result").text
    assert res_txt=="You entered: I am clicked"

