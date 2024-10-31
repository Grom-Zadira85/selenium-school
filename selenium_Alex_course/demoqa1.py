import time
from selenium.webdriver.common.by import By

from selenium_Alex_course.conftest import browser

url = "https://demoqa.com/text-box"

def test_text_box(browser):
    browser.get(url)
    full_name = browser.find_element(By.XPATH, '//*[@placeholder="Full Name"]')
    full_name.send_keys("Vas Kor")
    email = browser.find_element(By.XPATH, '//*[@placeholder="name@example.com"]')
    email.send_keys("gamma_h8@bk.ru")
    current_address = browser.find_element(By.XPATH, '//*[@placeholder="Current Address"]')
    current_address.send_keys("123\n321")
    permanent_address = browser.find_element(By.XPATH, '//*[@id="permanentAddress"]')
    permanent_address.send_keys("31\n345")
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = (browser.find_element(By.XPATH, '//*[@id="submit"]'))
    button.click()



#     check_field = browser.find_element(By.XPATH, '//*[@id="Ad.Plus-970x250-2"]')
#     text = """Name:Vas Kor
#
# Email:gamma_h8@bk.ru
#
# Current Address :123 321
#
# Permanent Address :31 345"""
#     assert check_field.text == text

    time.sleep(5)

def test_check(browser):
    browser.get("https://demoqa.com/checkbox")
    locate_home = browser.find_element(By.XPATH, '//*[@class="rct-title"][text()="Home"]')
    browser.execute_script("arguments[0].scrollIntoView();", locate_home)
    browser.find_element(By.CSS_SELECTOR, '[class="rct-icon rct-icon-expand-close"]').click()

    locate_home.click()
    time.sleep(5)
