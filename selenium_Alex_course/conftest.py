import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import allure


@allure.title('Test')
@pytest.fixture(scope="function")
def browser():
    options = ChromeOptions()
    options.add_argument("--window-size=1440,920")
    options.add_argument("--incognito")
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
