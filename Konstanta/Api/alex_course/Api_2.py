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
        files=("woolf".jpg, open("subfolder/woolf.jpg", "rb"))

    )

    print(response.status_code)
    print(response.json())
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(formatted_response)


