import time

from selenium.webdriver.common.by import By

url = "http://the-internet.herokuapp.com/dropdown"


def test_drop_down(browser):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, '[id="dropdown"]').click()
    time.sleep(3)

    value1 = browser.find_element(By.CSS_SELECTOR, '[value = "1"]')
    value1.click()
    time.sleep(3)
    assert value1.text == "Option 1"

    value2 = browser.find_element(By.CSS_SELECTOR, '[value = "2"]')
    value2.click()
    time.sleep(3)

    assert value2.text == "Option 2"












