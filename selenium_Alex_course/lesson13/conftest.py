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
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36")

    return options


@allure.title('Test')
@pytest.fixture(scope="function")
def browser(chrome_options):
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()
