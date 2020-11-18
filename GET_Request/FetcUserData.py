import requests

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response)
