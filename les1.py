import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()

# driver.get("https://demoqa.com/automation-practice-form")
# PAGE_TITLE = driver.title
# print(PAGE_TITLE)
# driver.refresh()
#
# driver.back()
# time.sleep(1)
# assert driver.current_url == "data:,"
# driver.forward()
# assert driver.current_url == "https://demoqa.com/automation-practice-form"


link = "https://demoqa.com/automation-practice-form"


def test_4_6(browser):
    browser.get(link)
    PAGE_TITLE = browser.title
    print(PAGE_TITLE)
    browser.refresh()

    browser.back()
    time.sleep(1)
    assert browser.current_url == "data:,"
    browser.forward()
    assert browser.current_url == "https://demoqa.com/automation-practice-form"
