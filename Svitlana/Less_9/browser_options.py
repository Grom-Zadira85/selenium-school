import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager" #"normal"
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors") #обход ошибки сертификата
chrome_options.add_argument("--window-size=1920,1080") # изменение размера окна, хорошо использовать в опциях
# chrome_options.add_argument("--disable-cache") # кеш не будет записываться!
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()

driver.get("https://whatismyipaddress.com/")

end_time = time.time()
result = end_time - start_time
print(result)

# time.sleep(3)
