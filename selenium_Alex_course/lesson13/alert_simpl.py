import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_alert(browser):
    browser.get("https://demoqa.com/alerts")
    BUTTON_4 = browser.find_element(By.CSS_SELECTOR, "[id='promtButton']")
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='promtButton']")))

    browser.execute_script("arguments[0].scrollIntoView();", BUTTON_4)
    BUTTON_4.click()

    # Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
    WebDriverWait(browser, 15).until(EC.alert_is_present())

    # Ввод данных в alert
    prompt = browser.switch_to.alert
    time.sleep(3)
    prompt.send_keys("My answer")
    time.sleep(3)

    print(prompt.text)
    prompt.accept()
    time.sleep(3)
