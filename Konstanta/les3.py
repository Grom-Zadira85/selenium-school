import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://victoretc.github.io/selenium_waits/"


def test_text_box(browser):
    browser.get(url)
    browser.find_element(By.XPATH, '[//*[text()="Начать тестирование"]').click()
    #
    # browser.find_element(By.CSS_SELECTOR, '[id="login"]').send_keys("login")
    # browser.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys("password")
    #
    # browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
    #
    # browser.find_element(By.CSS_SELECTOR, '[id="register"]').click()

    time.sleep(4)

