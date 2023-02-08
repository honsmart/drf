import requests

endpoint = "http://127.0.0.1:8000/"

get_response = requests.get(endpoint, json={"query": "Hello world"}) 

print(get_response.status_code)
# print(get_response.json())
print(get_response.text)