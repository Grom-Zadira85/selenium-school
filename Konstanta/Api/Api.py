import requests
import json
import pandas as pd
import xml.etree.ElementTree as et


def test1():
    # Запрос GET (Отправка только URL без параметров)
    response = requests.get("http://api.open-notify.org/astros.json")

    # Вывод статус кода
    print(response.status_code)

    # Вывод ответа, полученного от сервера API
    print(response.json())


def test_json_print():
    # Запрос GET (Отправка только URL без параметров)
    response = requests.get("http://api.open-notify.org/astros.json")

    # Вывод ответа, через пользовательскую функцию jprint
    print(response.json())

    # создаем форматированную строку объекта Python JSON
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(text)


def test2():
    response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")

    # Вывод ответа, через пользовательскую функцию json_print
    print("response:\n{}\n\n".format(response))
    print("response.url:\n{}\n\n".format(response.url))  # Посмотреть формат URL (с параметрами)
    print("response.headers:\n{}\n\n".format(response.headers))  # Header of the request
    print("response.status_code:\n{}\n\n".format(response.status_code))  # Получить код ответа
    print("response.text:\n{}\n\n".format(response.text))  # Text Output
    print("response.encoding:\n{}\n\n".format(response.encoding))  # Узнать, какую кодировку использует Requests
    print("response.content:\n{}\n\n".format(response.content))  # В бинарном виде
    print("response.json():\n{}\n\n".format(response.json()))  # JSON Output


"""Получаем данные по вакансиям с сайта hh.ru через API с помощью Python Requests Get
У сайта hh есть API, вся свежая информация находится на сайте https://dev.hh.ru/ 
и в документации https://github.com/hhru/api. В рамках примера будет использован метод vacancies."""


def test3():
    page_number = 0
    search_str = "qlik"
    area_str = "1"

    # Адрес api метода для запроса get
    url = 'https://api.hh.ru/vacancies'
    param = {
        "text": search_str,
        "area": area_str,
        "page": page_number
    }

    # Отправляем get request (запрос GET)
    response = requests.get(url, param)
    data = response.json()

    # Создаем пустой dict (словарь данных)
    dict_data = {}
    dict_number = 0

    # Количество страниц
    for i in range(0, data['pages']):
        param_cycle = {
            "text": search_str,
            "area": area_str,
            "page": i
        }
        response_cycle = requests.get(url, param_cycle)
        print("ЗАПРОС №" + str(i))
        result = dict(response_cycle.json())
        result = result['items']

        # Парсим исходный list формата Json в dictionary (словарь данных)
        for y in range(0, len(result) - 1):
            dict_data[dict_number] = {
                'id': result[y]['id'],
                'premium': result[y]['premium'],
                'name': result[y]['name'],
                'department': result[y]['department'],
                'has_test': result[y]['has_test'],
                'area_name': result[y]['area']['name'],
                'salary': result[y]['salary'],
                'type_name': result[y]['type']['name'],
                'snippet_requirement': result[y]['snippet']['requirement']
            }
            dict_number = dict_number + 1

        print("==================================")
    print(dict_data[0])


def test_get():
    v_date = '16.04.2020'
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    params = {'date_req': v_date}

    # Отправляем GET запрос с отключенной проверкой сертификата
    response = requests.get(url, params=params, verify=False)

    # Обработка XML-ответа
    tree = et.ElementTree(et.fromstring(response.text))
    root = tree.getroot()
    df_cols = ["date", "numcode", "charcode", "nominal", "name", "value"]
    rows = []
    for node in root:
        s_numcode = node.find("NumCode").text if node is not None else None
        s_charcode = node.find("CharCode").text if node is not None else None
        s_nominal = node.find("Nominal").text if node is not None else None
        s_name = node.find("Name").text if node is not None else None
        s_value = node.find("Value").text if node is not None else None

        rows.append({
            "date": v_date,
            "numcode": s_numcode,
            "charcode": s_charcode,
            "nominal": s_nominal,
            "name": s_name,
            "value": s_value
        })

    # Создаем DataFrame и выводим первые строки
    df = pd.DataFrame(rows, columns=df_cols)
    print(df.head())

"""
Этот код выполняет запрос к API Центрального банка России, чтобы получить данные о валютных курсах на определенную дату,
 обрабатывает XML-ответ и сохраняет данные в формате таблицы (DataFrame) с использованием pandas. 


Определение даты и URL:

v_date = '16.04.2020'
url = 'https://www.cbr.ru/scripts/XML_daily.asp'
params = {'date_req': v_date}
Здесь задается дата v_date и URL для получения данных о валютных курсах на эту дату. Параметр params определяет 
параметры запроса, в данном случае date_req указывает дату, за которую запрашиваются курсы валют.

Выполнение GET-запроса:
response = requests.get(url, params=params, verify=False)
Функция requests.get() выполняет GET-запрос к указанному URL с параметром params. 
verify=False отключает проверку сертификата SSL (для тестирования).

Обработка XML-ответа:
tree = et.ElementTree(et.fromstring(response.text))
root = tree.getroot()
Эта часть кода разбирает XML-ответ. response.text содержит тело ответа в виде текста XML. et.fromstring() 
преобразует его в XML-дерево, которое затем оборачивается в объект ElementTree для дальнейшей обработки.

Создание списка строк данных:
df_cols = ["date", "numcode", "charcode", "nominal", "name", "value"]
rows = []
for node in root:
    s_numcode = node.find("NumCode").text if node is not None else None
    s_charcode = node.find("CharCode").text if node is not None else None
    s_nominal = node.find("Nominal").text if node is not None else None
    s_name = node.find("Name").text if node is not None else None
    s_value = node.find("Value").text if node is not None else None

    rows.append({
        "date": v_date,
        "numcode": s_numcode,
        "charcode": s_charcode,
        "nominal": s_nominal,
        "name": s_name,
        "value": s_value
    })
Здесь создается список строк данных rows, где каждая строка представляет информацию о валюте. 
Цикл for перебирает каждый элемент node (представляющий отдельную валюту) в XML. node.find("...").text извлекает 
текстовые данные каждого элемента (например, NumCode, CharCode, Nominal, Name, Value), а затем добавляет их в словарь, 
представляющий одну строку данных. Каждая строка добавляется в rows.


Создание и вывод DataFrame:
df = pd.DataFrame(rows, columns=df_cols)
print(df.head())
Наконец, создается объект DataFrame из списка rows с определенными столбцами (df_cols). df.head() выводит первые строки 
таблицы, показывая полученные данные в удобочитаемом формате.
"""

"======= Мы можем отправить запрос POST с помощью метода requests.post() следующим образом: ==========================="

BASE_URL = 'https://fakestoreapi.com'

new_product = {
        "title": 'test product',
        "price": 13.5,
        "description": 'lorem ipsum set',
        "image": 'https://i.pravatar.cc',
        "category": 'electronic'
    }


def test_post_1():
    response = requests.post(f"{BASE_URL}/products", json=new_product)
    print(response.json())
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(text)


""" Строка text = json.dumps(response.json(), sort_keys=True, indent=4) выполняет следующие шаги:
response.json() — эта часть извлекает данные JSON из ответа response. requests.get() возвращает объект response, 
и метод .json() преобразует тело ответа в Python-объект (обычно это словарь или список), 
если сервер вернул данные в формате JSON.

json.dumps(..., sort_keys=True, indent=4) — функция json.dumps() преобразует Python-объект (словарь, список и т.д.) 
в строку формата JSON. 

Параметры в ней выполняют следующие функции:
sort_keys=True — сортирует ключи JSON по алфавиту, что упрощает чтение и сопоставление данных.
indent=4 — добавляет отступы в 4 пробела для форматирования JSON, делая его более читаемым для человека."""