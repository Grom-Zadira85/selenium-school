import time
from tabnanny import check

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_check_box(browser):
    browser.get("https://demoqa.com/checkbox")
    browser.find_element(By.XPATH, '(//*[@class="rct-collapse rct-collapse-btn"])[1]').click()
    browser.find_element(By.CSS_SELECTOR, '[class="rct-checkbox"]').click()
    check_box_3 = browser.find_element(By.XPATH, '(//*[@class="rct-checkbox"])[3]')
    check_box_3.click()

    time.sleep(3)

    assert check_box_3.is_selected() == False, "chect_box_is_checked"







