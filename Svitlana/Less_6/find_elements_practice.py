import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get("https://hyperskill.org/tracks")
#
# time.sleep(5)
#
# # print(len(driver.find_elements("class name", "nav-link"))) #поиск всех элементов класса nav-link
#
# driver.find_elements("class name", "nav-link")[2].click() #нажатие на 3 элемент в списке (индекс 2)
#
# time.sleep(3)

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(5)

# print(len(driver.find_elements("class name", "nav-link"))) #поиск всех элементов класса nav-link

driver.find_element("class name", "wikipedia-icon").click() #нажатие на 3 элемент в списке (индекс 2)

time.sleep(3)


