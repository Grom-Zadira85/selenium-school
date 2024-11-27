import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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

def test_drop_down2(browser):
    # Открыть страницу
    browser.get("https://demoqa.com/select-menu")

    # Работа с первым выпадающим списком
    # Находим первый выпадающий список и кликаем по нему
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//*[@class=" css-1hwfws3"])[1]'))
    )
    dropdown.click()

    # Ждем появления опций и выбираем "Group 2, option 2"
    option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Group 2, option 2']"))
    )
    option.click()

    # Небольшая пауза для наглядности (опционально)
    time.sleep(2)

    # Работа со вторым выпадающим списком
    # Находим поле ввода второго списка
    dd2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[id="react-select-3-input"]'))
    )

    # Вводим значение "Mrs."
    dd2.send_keys("Mrs.")

    # Добавляем паузу, чтобы проверить, что значение вводится (опционально)
    time.sleep(2)

    # Нажимаем Enter, чтобы выбрать опцию
    dd2.send_keys("\n")

    # Еще небольшая пауза для проверки (опционально)
    time.sleep(2)


def test_drop_down3(browser):
    browser.get("https://demoqa.com/select-menu")
    # browser.find_element(By.CSS_SELECTOR, '[id="oldSelectMenu"]')
    browser.find_element(By.CSS_SELECTOR, '[value="2"]').click()
    time.sleep(3)
    MS = browser.find_element(By.CSS_SELECTOR, '[id="react-select-4-input"]')
    MS.send_keys("Gre")
    time.sleep(3)
    assert MS.get_attribute("value") == "Gre"
    MS.send_keys(Keys.ENTER)
    time.sleep(3)

    MS2 = browser.find_element(By.CSS_SELECTOR, '[value="audi"]')
    browser.execute_script("arguments[0].scrollIntoView();", MS2)
    browser.find_element(By.CSS_SELECTOR, '[value="audi"]').click()
    time.sleep(6)
    assert MS2.get_attribute("value") == "audi"

    time.sleep(3)

















