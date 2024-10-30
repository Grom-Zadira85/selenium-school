import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

url = "https://demoqa.com/text-box"


def test_text_box(browser):
    browser.get(url)
    full_name = browser.find_element(By.XPATH, '//*[@placeholder="Full Name"]')
    full_name.send_keys("Konstanta")

    email = browser.find_element(By.XPATH, '//*[@placeholder="name@example.com"]')
    email.send_keys("Grom_Zadira@p.ru")

    current_address = browser.find_element(By.XPATH, '//*[@placeholder="Current Address"]')
    current_address.send_keys("Ukraine")

    permanent_address = browser.find_element(By.XPATH, '//*[@id="permanentAddress"]')
    permanent_address.send_keys("Ukraine")

    button = browser.find_element(By.XPATH, '//*[@id="submit"]')
    browser.execute_script("arguments[0].scrollIntoView();", button)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]')))
    button.click()

    check_field = browser.find_element(By.XPATH, '//*[@class="border col-md-12 col-sm-12"]')

    expected_text = (
        "Name:Konstanta\n"
        "Email:Grom_Zadira@p.ru\n"
        "Current Address :Ukraine\n"
        "Permananet Address :Ukraine"
    )

    assert check_field.text == expected_text, f"Expected '{expected_text}', but got '{check_field.text}'"
    time.sleep(2)
