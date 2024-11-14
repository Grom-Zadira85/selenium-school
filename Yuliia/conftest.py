import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def chrome_options():
    options = ChromeOptions()
    # options.add_argument("--window-size=1440,920")
    options.add_argument("--incognito")
    options.add_argument("--disable-cache")
    options.add_argument('--start-maximized')
    return options


@allure.title('Test')
@pytest.fixture(scope="function")
def browser(chrome_options):
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()
