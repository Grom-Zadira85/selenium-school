import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#driver = webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")
PAGE_TITLE = driver.title
time.sleep(5)
print(PAGE_TITLE)


driver.back()
time.sleep(2)
assert driver.current_url == "data:,"
driver.forward()
assert driver.current_url == "https://demoqa.com/automation-practice-form"