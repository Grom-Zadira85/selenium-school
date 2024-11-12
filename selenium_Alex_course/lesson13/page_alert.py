import time

from selenium.webdriver.common.by import By
from .locators import AlertPage
from selenium.webdriver.chrome.webdriver import WebDriver

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
        self.browser.find_element(*AlertPage.Click_Button_To_See_Alert).click()
        time.sleep(2)
        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(2)

    def click_alert_after_5_seconds(self):
        self.browser.find_element(*AlertPage.After_5_seconds).click()
        time.sleep(2)
        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(2)
