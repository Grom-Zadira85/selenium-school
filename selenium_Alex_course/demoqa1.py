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


    assert browser.find_element(By.CSS_SELECTOR, '[class="rct-checkbox"]').is_selected() is True


def test_field(browser):
    browser.get("https://demoqa.com/text-box")
    browser.find_element(By.CSS_SELECTOR, '[placeholder = "Full Name"]').send_keys("Olga")
    browser.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys("olga@gmail.com")
    browser.find_element(By.CSS_SELECTOR, '[id="currentAddress"]').send_keys("Wroclaw")
    browser.find_element(By.CSS_SELECTOR, '[id="permanentAddress"]').send_keys('Warsaw')


    time.sleep(2)
    button = browser.find_element(By.XPATH, '//*[text()="Submit"]')
    browser.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    time.sleep(2)

    check_field = browser.find_element(By.CSS_SELECTOR, '[class="border col-md-12 col-sm-12"]')

    expected_text = (
    "Name:Olga\n"
    "Email:olga@gmail.com\n"
    "Current Address :Wroclaw\n"
    "Permananet Address :Warsaw")



    assert check_field.text == expected_text



