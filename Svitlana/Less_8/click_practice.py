import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

name_field = driver.find_element("xpath", "//input[@id='userName']")
name_field.clear()
assert name_field.get_attribute("value") == ""
name_field.send_keys("Greys")
assert "Greys" in name_field.get_attribute("value")
print(name_field.get_attribute("value"))

email_field = driver.find_element("xpath", "//input[@id='userEmail']")
email_field.clear()
assert email_field.get_attribute("value") == ""
email_field.send_keys("12ewe@gmail.com")
assert "12ewe@gmail.com" in email_field.get_attribute("value")

print(email_field.get_attribute("value"))
time.sleep(3)
# email_field.clear()
