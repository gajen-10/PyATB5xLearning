import pytest
import allure

from selenium import webdriver


@allure.title("Open the app.vwo.com")
@pytest.mark.regression

def test_vwo_login():
    driver=webdriver.Chrome()
    #1. This code is translated into the API request
    #2. Post request- Browser Webdriver (Server)
    #3. Where it will create a session or Fresh copy Browser(Chrome)
    #4. Session ID - 16 digit() will be created
    driver.get("https/:vwo.app.com")
    #5. GET -> GET API request to navigate to particular page
    #6. browser will navigate to the URL

    # Source code(Client) -> API Request(W3C) -> Browser Driver(Server) ->Browser


