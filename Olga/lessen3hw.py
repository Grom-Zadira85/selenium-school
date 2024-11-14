import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = "https://victoretc.github.io/selenium_waits/"
LOGIN = "Olga"
PASSWORD = "olg1"


def test_registrater(browser):
    browser.get(url)
    button_start = browser.find_element(By.CSS_SELECTOR, '[id="startTest"]')

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(button_start)).click()

    login = browser.find_element(By.CSS_SELECTOR, '[id="login"]')
    password = browser.find_element(By.CSS_SELECTOR, '[id="password"]')

    login.send_keys(LOGIN)
    password.send_keys(PASSWORD)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[id="agree"]')
    button_registr = browser.find_element(By.CSS_SELECTOR, '[id="register"]')

    checkbox.click()
    button_registr.click()



    success_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="successMessage"]')))

    assert f'{success_message.text == "Вы успешно зарегистрированы!"}, success_message!="Вы успешно зарегистрированы!'

    time.sleep(5)













