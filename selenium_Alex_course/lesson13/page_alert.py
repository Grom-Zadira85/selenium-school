import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import AlertPage

# class Url():
#     URL = "https://demoqa.com/alerts"

url = "https://demoqa.com/alerts"


class BasePage:
    def __init__(self, browser: WebDriver, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def click_button_to_see_alert(self):
        """Принять  alert"""
        self.browser.find_element(*AlertPage.Click_Button_To_See_Alert).click()
        time.sleep(2)
        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(2)

    def click_alert_after_5_seconds(self):
        """  Установка Ожидания в alert  """
        self.browser.find_element(*AlertPage.After_5_seconds).click()
        wait = WebDriverWait(self.browser, 8)  # Ожидание 8 секунд
        alert = wait.until(EC.alert_is_present())  # Ожидаем, пока алерт появится
        alert.accept()  # Подтверждаем алерт
        time.sleep(2)

    def confirm_box_wll_appear(self):
        """Принять или отклонить alert"""
        button3 = self.browser.find_element(*AlertPage.Confirm_Box_Will_Appear)
        self.browser.execute_script("arguments[0].scrollIntoView();", button3)
        button3.click()
        time.sleep(2)

        alert = self.browser.switch_to.alert
        # alert.accept()
        alert.dismiss()
        time.sleep(2)

    def prompt_box_will_appear(self):
        """  Ввод данных в alert и Получение текста из alert """
        button4 = self.browser.find_element(*AlertPage.Prompt_Box_Will_Appear)

        self.browser.execute_script("arguments[0].scrollIntoView();", button4)
        button4.click()

        WebDriverWait(self.browser, 10).until(EC.alert_is_present())

        alert = self.browser.switch_to.alert
        alert.send_keys("Hi Admin")
        print(alert.text)
        time.sleep(2)
        alert.accept()
        time.sleep(2)
