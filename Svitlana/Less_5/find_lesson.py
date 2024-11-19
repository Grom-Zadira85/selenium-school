import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/pl/login?site_tag=FCC_HO_1_H")

time.sleep(5)
# print(type(driver.find_element("id", "loginformsubmit")))

driver.find_element("id", "loginformsubmit").click()

time.sleep(3)