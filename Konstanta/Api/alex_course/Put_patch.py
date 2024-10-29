import json

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

""" json который  указан в посте 1 -на апи  https://jsonplaceholder.typicode.com/posts
{ "userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", 
"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas 
totam\nnostrum rerum est autem sunt rem eveniet architecto" },"""


def test_put():
    response = requests.put(
        url=f'{BASE_URL}/posts/1',
        json={
            "title": "Wither_3"  # Заменим заголовок статьи. Передаем в json поля - которые хотим обновить
        },
    )

    print(response.status_code)
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(formatted_response)


""" метод put меняет информацию  в статье на ту что мы отправим, но  в json будет не полное тело  ресурса по сравнению с  
 прошлым json во время метода POST. 
 После нашего изменения из-за не полного объема тела отправки, мы обнуляем все остальные поля . 
 В дальнейшем метод put будут удалять  для работы с Api """

""" То что выдал терминал 
=======================================================================================================
Put_patch.py::test_put PASSED                   [100%]200
{
    "id": 1,
    "title": "Wither_3"
}
===========================================================================================================
Потерялся  "userId": 1,
============================================================================================================="""


def test_patch():
    response = requests.patch(
        url=f'{BASE_URL}/posts/1',
        json={
            "title": "Wither_3 -The best game!!!"
        },
    )

    print(response.status_code)
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(formatted_response)


""" Вывод терминала Put_patch.py::test_patch PASSED             [100%]200 { "body": "quia et suscipit\nsuscipit 
recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem 
eveniet architecto", "id": 1, "title": "Wither_3 -The best game!!!", "userId": 1 }


Вернулись все поля тела с изменен6ием в поле title 
"""


def test_patch_2():
    response = requests.patch(
        url=f'{BASE_URL}/posts/1',
        json={
            "title": "Wither_3 -The best game!!!",
            "body": "Play the game after reading all the books by Andrzej Sapkowski."
        },

    )

    print(response.status_code)
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    print(formatted_response)
