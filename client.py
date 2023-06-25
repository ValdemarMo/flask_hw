import requests


response = requests.post(
    "http://127.0.0.1:5000/ad",
    json={
        "owner": "Creator",
        "title": "Kill all people!!",
        "description": "Grrrrrrrr!",
    },
)
print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:5000/ad/1")
print(response.status_code)
print(response.text)

response = requests.delete("http://127.0.0.1:5000/ad/1" "")
print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:5000/ad/1")
print(response.status_code)
print(response.text)
