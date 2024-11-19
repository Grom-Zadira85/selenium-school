import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://demoqa.com/text-box"


def test_text_box(browser):
    browser.get(url)
    full_name = browser.find_element(By.XPATH, '//*[@placeholder="Full Name"]')
    full_name.send_keys("Konstanta")

    email = browser.find_element(By.XPATH, '//*[@placeholder="name@example.com"]')
    email.send_keys("Grom_Zadira@p.ru")

    current_address = browser.find_element(By.XPATH, '//*[@placeholder="Current Address"]')
    current_address.send_keys("Ukraine")

    permanent_address = browser.find_element(By.XPATH, '//*[@id="permanentAddress"]')
    permanent_address.send_keys("Ukraine")

    button = browser.find_element(By.XPATH, '//*[@id="submit"]')
    browser.execute_script("arguments[0].scrollIntoView();", button)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]')))
    button.click()

    check_field = browser.find_element(By.XPATH, '//*[@class="border col-md-12 col-sm-12"]')

    expected_text = (
        "Name:Konstanta\n"
        "Email:Grom_Zadira@p.ru\n"
        "Current Address :Ukraine\n"
        "Permananet Address :Ukraine"
    )

    assert check_field.text == expected_text, f"Expected '{expected_text}', but got '{check_field.text}'"
    time.sleep(2)


def test_check_box(browser):
    browser.get("https://demoqa.com/checkbox")

    check_icon = browser.find_element(By.CSS_SELECTOR, '[class="rct-icon rct-icon-uncheck"]')
    check_icon.click()

    toggle = browser.find_element(By.CSS_SELECTOR, '[class="rct-icon rct-icon-expand-close"]')
    toggle.click()

    # Найти все отмеченные чекбоксы
    checked_icons = browser.find_elements(By.CSS_SELECTOR, '[class="rct-icon rct-icon-check"]')
    time.sleep(2)

    # Выведем статус чек-бокса True/False, так как он меняется при клике на элемент, отвечающий за выставление флажка
    HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")
    print(browser.find_element(*HOME_CHECKBOX).is_selected())

    # Проверка, что хотя бы один чекбокс был отмечен
    assert len(checked_icons) > 0, "Не удалось отметить чек-боксы"

    time.sleep(2)

""" 
# assert CHECK_BOX.get_attribute("checked") is not None
# assert CHECK_BOX.is_selected() is True

В вашей функции test_check_box возникла ошибка из-за использования assert CHECK_BOX.is_selected().
 Это происходит потому, что is_selected() работает только для элементов типа <input type="checkbox">, 
 тогда как в данном случае CHECK_BOX — это не сам чекбокс, а иконка, которая визуально показывает его состояние."""

"""
Чтобы выбрать первый элемент с классом rct-icon rct-icon-expand-open, используя XPath, 
можно воспользоваться следующим выражением:
(//*[@class="rct-icon rct-icon-expand-open"])[1]


====== Для доступа по порядковому номеру, необходимо использовать [n], все как в Python) Но есть пара нюансов!=======

Допустим, у нас есть HTML-код и нам необходимо найти div с текстом 2:

<root>
    <header>
        <div>1</div>
        <div>2</div>
        <section>
            <div>3</div>
            <div>4</div>
        </section>
    </header>
</root>
Казалось бы, если мы напишем такой запрос:
 //header//div[2] то получим второй div внутри header, как раз который нам нужен, но нет! 
 Мы получим "Каждый второй div лежащий внутри header"

Такой способ в изучаемом нами подходе не будет работать и врятли пригодиться, ибо нам вернуться 2 div блока, 
а нам нужно немного другое!

--------------------Мы напишем следующий Xpath: (//header//div)[2]  --------------------------------------------

Разобьем по частям, чтобы было понятнее:
1. (//header//div) - как вы видите стоят скобки, они вернут нам список всех div-блоков внутри header.
Пример для наглядности: (<div>1</div>, <div>2</div>, <div>3</div>, <div>4</div>)

2. (//header//div)[2] - тут мы получаем второй div из полученного списка и все работает)
Важно: индексация элементов в Xpath идет не с 0 как в Python, а с 1


pytest -s -v selenium_Alex_course/demoqa.py::test_check_box --alluredir=./reports

=======================================================================================================================
"""
