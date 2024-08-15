import requests


response = requests.post("http://localhost:5413/api/addition", json={"x": "avbs", "y": 24})
print(response.status_code)
print(response.json())