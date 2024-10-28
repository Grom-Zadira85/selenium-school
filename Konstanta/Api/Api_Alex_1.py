import requests
import json
# from requests.auth import HTTPBasicAuth

BASE_URL = "https://petstore.swagger.io/v2"

response = requests.get(
    url=f'{BASE_URL}/store/inventory',  # Endpoint

    # auth=HTTPBasicAuth("username", "password")
    # params={},  # query parameters для сортировок,  для выборок. Прокидываются в url
    # verify=False,  # принимает True или False. Проверка Сертификата. Предположительно ssl/tls

    headers={
        "api_key": "special-key"
    },  # передаем токены
)

# # СТАТУС КОД НАДО ВЫВОДИТЬ ДО ПЕРЕВОДА В КАКОЙ ЛИБО ФОРМАТ (JSON,DUMP)
# НЕ РАБОТАЕТ ЕСЛИ RESPONSE В ВИДЕ STR
# print(response.status_code)

# вывод значения по ключу "sold" из списка json

# задаем ответ по умолчанию json
# response = response.json()

# print(response["sold"])
# print(response)

"============================2-Й ВАРИАНТ==================================================================="
# СТАТУС КОД НАДО ВЫВОДИТЬ ДО ПЕРЕВОДА В КАКОЙ ЛИБО ФОРМАТ
print(response.status_code)
print(f' Статус код ответа {response.status_code}')
response = json.dumps(response.json(), sort_keys=True, indent=4)
print(response)




