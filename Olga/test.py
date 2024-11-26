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




import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_drop_down2(browser):
    # Open the target URL
    browser.get("https://demoqa.com/select-menu")

    # Locate and click the dropdown to open it
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//*[@class=" css-1hwfws3"])[1]'))
    )
    dropdown.click()

    # Wait for the options to load and locate the desired option
    option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Group 2, option 2']"))
    )

    # Click the desired option
    option.click()

    # Add a short sleep for observation (optional)
    time.sleep(3)










