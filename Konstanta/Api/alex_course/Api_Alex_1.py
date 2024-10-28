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

# # СТАТУС КОД НАДО ВЫВОДИТЬ ДО ПЕРЕВОДА В КАКОЙ ЛИБО ФОРМАТ (JSON,DUMP), НЕ РАБОТАЕТ ЕСЛИ RESPONSE В ВИДЕ STR
# print(response.status_code)

# задаем ответ по умолчанию json
# response = response.json()

# вывод значения по ключу "sold" из списка json
# print(response["sold"])
# print(response)

"============================2-Й ВАРИАНТ==================================================================="
# СТАТУС КОД НАДО ВЫВОДИТЬ ДО ПЕРЕВОДА В КАКОЙ ЛИБО ФОРМАТ
print(response.status_code)
print(f' Статус код ответа {response.status_code}')
response = json.dumps(response.json(), sort_keys=True, indent=4)
print(response)

"---------------------------------------------------------------------------------------------------------"

" ==========================================   Регистрация пользователя  ===================================="


def test_registration_user():
    response = requests.post(
        url=f'{BASE_URL}/user/createWithList',
        headers={
            "api_key": "special-key",
        },
        json=[
            {
                "id": 85,
                "username": "Grom",
                "firstName": "Konstanta",
                "lastName": "Konstanta",
                "email": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 0
            }
        ]
    )
    print(response.status_code)
    print(response)


"============================================================================================================="

username = "Grom"
password = "string"


def test_check_registration():
    response = requests.get(
        url=f'{BASE_URL}/user/{username}',
        headers={
            "api_key": "special-key"
        },
    )
    print(f'{response.status_code}')
    response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(response)


"======================  querry parameters ==========================================================================="


def test_get_pet_by_status():
    response = requests.get(
        url=f'{BASE_URL}/pet/findByStatus',
        headers={
            "api_key": "special-key"
        },
        params={
            "status": "sold"
        }
    )
    print(f'{response.status_code}')
    response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(response)
