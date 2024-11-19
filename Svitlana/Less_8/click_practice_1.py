import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://the-internet.herokuapp.com/status_codes")

links = driver.find_elements(By.TAG_NAME, "a")

links_to_click = [link.get_attribute("href") for link in links if "status_codes" in link.get_attribute("href")]

for link in links_to_click:
    driver.get(link)  # Navigate to the link
    print(link)
    time.sleep(2) # Optional: wait to let the page load

    # Here, add any additional actions or assertions

    driver.back()  # Navigate back to the starting page
    time.sleep(1)  # Optional: small wait to ensure the page loads

# Close the browser after all links are clicked
driver.quit()