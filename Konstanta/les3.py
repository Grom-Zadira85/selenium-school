import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv


url = "https://victoretc.github.io/selenium_waits/"
load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


def test_text_box(browser):
    browser.get(url)

    test_start = browser.find_element(By.XPATH, '//*[@id="startTest"]')

    WebDriverWait(browser, 15).until(EC.element_to_be_clickable(test_start))
    test_start.click()

    login = browser.find_element(By.CSS_SELECTOR, '[id="login"]')
    login.send_keys(LOGIN)

    password = browser.find_element(By.CSS_SELECTOR, '[id="password"]')
    password.send_keys(PASSWORD)

    check_box = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    check_box.click()

    browser.find_element(By.CSS_SELECTOR, '[id="register"]').click()

    test_start.click()

    assert f'Expected {login.get_attribute("value") == LOGIN}, value != LOGIN'
    assert f'Expected {password.get_attribute("value") == PASSWORD}, value != PASSWORD'

    print(check_box.is_selected())
    assert f'Expected {check_box.is_selected()}, check box is not pushed'

    success_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="successMessage"]')))
    assert f'{success_message.text == "Вы успешно зарегистрированы!"}, success_message!="Вы успешно зарегистрированы!'


def test_text_box_2(browser):
    browser.get(url)
    browser.implicitly_wait(15)
    test_start = browser.find_element(By.XPATH, '//*[@id="startTest"]')

    test_start.click()

    login = browser.find_element(By.CSS_SELECTOR, '[id="login"]')
    login.send_keys(LOGIN)

    password = browser.find_element(By.CSS_SELECTOR, '[id="password"]')
    password.send_keys(PASSWORD)

    check_box = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    check_box.click()

    browser.find_element(By.CSS_SELECTOR, '[id="register"]').click()

    test_start.click()

    assert f'Expected {login.get_attribute("value") == LOGIN}, value != LOGIN'
    assert f'Expected {password.get_attribute("value") == PASSWORD}, value != PASSWORD'

    print(check_box.is_selected())
    assert f'Expected {check_box.is_selected()}, check box is not pushed'

    time.sleep(5)
    success_message = browser.find_element(By.CSS_SELECTOR, '[id="successMessage"]')
    assert f'{success_message.text == "Вы успешно зарегистрированы!"}, success_message!="Вы успешно зарегистрированы!'
