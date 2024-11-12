import time
import os
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/status_codes"


def test_click_status_code(browser):
    browser.get(url)

    browser.find_element(By.CSS_SELECTOR, '[href="status_codes/200"]').click()
    time.sleep(3)
    browser.back()
    time.sleep(3)

    browser.find_element(By.CSS_SELECTOR, '[href="status_codes/301"]').click()
    time.sleep(3)
    browser.back()
    time.sleep(3)


" ============================Урок 10 загрузка файла ==========================="


def test_upload_file(browser):
    browser.get('https://demoqa.com/upload-download')

    browser.find_element(By.CSS_SELECTOR, "[id='uploadFile']").send_keys('C:/Users/konst/Downloads/БП/bp-atx-6.jpg')
    time.sleep(3)


"""

Чтобы решить эту проблему, вы можете изменить строку пути, используя один из следующих методов:

Замените обратные слэши на прямые:
browser.find_element(By.XPATH, "//input[@id='uploadFile']").send_keys('C:/Users/konst/Downloads/БП/bp-atx-6.jpg')

Используйте двойные обратные слэши:
browser.find_element(By.XPATH, "//input[@id='uploadFile']").send_keys('C:\\Users\\konst\\Downloads\\БП\\bp-atx-6.jpg')

Укажите путь как «сырой» (raw) строку, добавив перед строкой r:
# browser.find_element(By.XPATH, "//input[@id='uploadFile']").send_keys(r'C:\ Users\konst\Downloads\БП\ bp-atx-6.jpg') 
(в код записать без  без пробелов) """


def test_upload_file_2(browser):
    """  работает если файл находится в проекте пайчарм """
    browser.get('https://demoqa.com/upload-download')
    time.sleep(1)

    # Формируем путь к файлу для загрузки
    file_path = os.path.join(os.getcwd(), "screen.png")

    # Отправляем файл в поле загрузки
    browser.find_element(By.XPATH, "//input[@id='uploadFile']").send_keys(file_path)
    time.sleep(3)


"""чтобы os.path.join(os.getcwd(), "bp-atx-6.jpg") сработала корректно и указала на существующий файл, 
файл bp-atx-6.jpg должен находиться в текущей рабочей директории проекта, из которой запускается скрипт. 
По умолчанию os.getcwd() возвращает путь к корневой папке проекта, когда вы запускаете скрипт в PyCharm.
Если bp-atx-6.jpg находится в подкаталоге проекта, например, в папке files, то вам нужно указать этот подкаталог в пути:

file_path = os.path.join(os.getcwd(), "files", "bp-atx-6.jpg")
Или можно указать относительный путь, исходя из расположения файла, например:

file_path = os.path.join(os.path.dirname(__file__), "bp-atx-6.jpg")
Это позволит избежать зависимости от текущей рабочей директории и загрузить файл, 
находящийся в одной папке с самим скриптом."""


def test_download_file(browser):
    browser.get('https://demoqa.com/upload-download')
    browser.find_element(By.XPATH, '(//a)[3]').click()
    browser.save_screenshot("screen.png")
    time.sleep(3)
