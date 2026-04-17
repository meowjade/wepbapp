import requests

print(requests.post("http://localhost:5000/form", params={"a":"b"}, data={"c": "d"}).json())