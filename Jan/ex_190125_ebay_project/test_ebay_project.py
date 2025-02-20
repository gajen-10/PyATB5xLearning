import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def test_ebay_print():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_eng=driver.find_element(By.XPATH,"//input[@title='Search']")
    search_eng.send_keys("macmini")

    search_button=driver.find_element(By.XPATH,"//span[@class='gh-search-button__label']")
    search_button.click()

    item_title=driver.find_elements(By.XPATH,"//div[@class='s-item__title']")
    item_price=driver.find_elements(By.XPATH,"//span[@class='s-item__price']")

    for item in item_title:
        print(item.text)

    for price in item_price:
        print(price.text)

