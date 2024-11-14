import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from Yuliia.conftest import browser

url="https://demoqa.com/text-box"

def test_check_box(browser):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR,'[placeholder="Full Name"]').send_keys("hay")

    browser.find_element(By.CSS_SELECTOR,'[placeholder="name@example.com"]' ).send_keys("uprf@ukr.net")
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, '[placeholder="Current Address"]').send_keys("Grimsby")
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR,'[id="permanentAddress"]').send_keys("London")
    time.sleep(2)

    browser.find_element(By.CSS_SELECTOR,'[id="submit"]').click()
    time.sleep(35)

    expected_text =(
       "Name:hay\n"
       "Email:uprf@ukr.net\n"
       "Current Address :Grimsby\n"
       "Permananet Address :London"
    )
    check_field = browser.find_element(By.XPATH, '//*[@class="border col-md-12 col-sm-12"]')
    assert check_field.text == expected_text
