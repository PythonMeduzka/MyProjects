import requests

response = requests.post("http://127.0.0.1:3000/api/courses/1", json={"name": "Golang", "videos": 13})
response = requests.post("http://127.0.0.1:3000/api/courses/2", json={"name": "PHP", "videos": 8})
print(response.json())
