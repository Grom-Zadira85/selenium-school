import requests
import json

# URL запроса преобразуется в формат https://api-server-name.com/methodname_get?key2=value2&key1=value1
param_request = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://api-server-name.com/methodname_get', params=param_request)
print(response)

# GET запрос с заголовком
url = 'https://api-server-name.com/methodname_get'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
print(response)

# POST запрос с параметрами в запросе
data = {'key': 'value'}
response = requests.post('https://api-server-name.com/methodname_post', data=data)
print(response)
# СТРОКИ 17 И 20 РАВНЫ МЕЖДУ СОБОЙ ПО ЗНАЧЕНИЯМ - другой способ записи
response = requests.post('https://api-server-name.com/methodname_post', data={'key': 'value'})
print(response)

# POST запрос с параметрами через кортеж
param_tuples = [('param1', 'value1'), ('param1', 'value2')]
response = requests.post('https://api-server-name.com/methodname_post', data=param_tuples)
print(response)

# POST запрос с параметрами через словарь
param_dict = {'param': ['value1', 'value2']}
response = requests.post('https://api-server-name.com/methodname_post', data=param_dict)
print(response)

# POST запрос с параметрами в формате JSON
url = 'https://api-server-name.com/methodname_post'
param_dict = {'param': 'data'}
response = requests.post(url, data=json.dumps(param_dict))
print(response)
