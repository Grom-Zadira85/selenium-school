import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

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


def test_drop_down_by_value(browser):
    browser.get(url)
    drop_down = browser.find_element(By.CSS_SELECTOR, '[id="dropdown"]')
    select_dd = Select(drop_down)

    select_dd.select_by_value("1")
    time.sleep(3)
    assert select_dd.first_selected_option.text == "Option 1"

    select_dd.select_by_value("2")
    time.sleep(3)
    # print(select_dd.options)

    options_text = [option.text for option in select_dd.options]
    print(f"Содержимое дропдауна: {options_text}")

    assert select_dd.first_selected_option.text == "Option 2"


def test_drop_down_by_index(browser):
    browser.get(url)
    drop_down = browser.find_element(By.CSS_SELECTOR, '[id="dropdown"]')
    select_dd = Select(drop_down)

    select_dd.select_by_index(1)
    time.sleep(1)
    assert select_dd.first_selected_option.text == "Option 1"

    select_dd.select_by_index(2)
    time.sleep(1)

    # не работает корректно print(select_dd.options)

    options_text = [option.text for option in select_dd.options]
    print(f"Содержимое дропдауна: {options_text}")

    assert select_dd.first_selected_option.text == "Option 2"


def test_keyboard(browser):
    browser.get("http://the-internet.herokuapp.com/key_presses")
    # input_field = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
    input_field = browser.find_element(By.XPATH, '//input')
    input_field.send_keys("All thees texts can be delete")
    time.sleep(2)
    assert input_field.get_attribute("value") == "All thees texts can be delete"

    input_field.send_keys(Keys.CONTROL + "A")
    input_field.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    assert input_field.get_attribute("value") == ""
