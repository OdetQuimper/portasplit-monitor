import requests
import math

response = requests.post(
    "https://braucheklima.de/api/availability",
    json=[],
    timeout=30
)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("content-type"))
print("Antwort:")
print(response.text[:1000])

data = response.json()
