import requests

r = requests.get("http://localhost:5000/hello{name}")
print(r.text)