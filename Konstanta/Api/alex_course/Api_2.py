import json

import requests
# from requests.auth import HTTPBasicAuth

BASE_URL = "https://petstore.swagger.io/v2"


def test_add_new_pet():
    response = requests.post(
        url=f'{BASE_URL}/pet',
        headers={
            "api_key": "special-key"
        },
        json={
            "id": 85,
            "category": {
                "id": 0,
                "name": "Woolf"
            },
            "name": "Wiedzmin",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "Wight woolf"
                }
            ],
            "status": "available"
        }
    )
    print(response.status_code)
    print(response.json())
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(formatted_response)


"========================================================================================================="

petId = 85


def test_get_pet_by_id():
    response = requests.get(
        url=f'{BASE_URL}/pet/{petId}',
        headers={
            "api_key": "special-key"
        },

    )

    print(response.status_code)
    print(response.json())
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(formatted_response)


"======================================================================================================="


def test_add_photo_pet_upload_image():
    response = requests.post(
        url=f'{BASE_URL}/pet/{petId}/uploadImage',
        headers={
            "api_key": "special-key"
        },
        files={
            "file": ("woolf.jpg", open(r"D:\My project PY\selenium-school\Konstanta\Api\alex_course\woolf.jpg", "rb"),
                     "image/jpg")
        }
    )
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Получаем JSON-ответ и проверяем, что он содержит сообщение про информацию о загруженном файле
    assert "File uploaded to" in response.json().get("message", ""), "File upload confirmation message not found"

    print(response.status_code)
    print(response.json())
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(formatted_response)

    """                response_json.get("message", ""):

response.json — это объект JSON, полученный из ответа сервера.
.get("message", "") — метод .get() извлекает значение ключа "message" из JSON. 
Если ключа "message" нет в ответе, по умолчанию будет возвращена пустая строка "".

                 File uploaded to" in response_json.get("message", ""):
Эта часть проверяет, что подстрока "File uploaded to" присутствует в значении "message". 
Иными словами, если сообщение о загрузке файла присутствует, эта проверка вернется True.
assert "File uploaded to" in response_json.get("message", ""), "File upload confirmation message not found":

Если условие не выполняется (в данном случае, если подстрока 
"File uploaded to" не найдена в "message"), assert выбрасывает ошибку и останавливает выполнение кода.

Если ошибка возникает, выведется сообщение "File upload confirmation message not found" для отладки.
В итоге  Эта строка проверяет, что в ответе содержится текст, подтверждающий, что файл был загружен."""