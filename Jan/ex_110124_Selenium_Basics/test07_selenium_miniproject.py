import pytest
import allure

from selenium import webdriver


@allure.title("Open the app.vwo.com")
@pytest.mark.regression

@allure.title("Verify the title of vwo.com is expected")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found !!, Testcase Passed!")

    else:
        print("Text not found on the webpage")
        pytest.fail("Text not found on the webpage")



