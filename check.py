import requests

r = requests.post(
    "https://braucheklima.de/api/availability",
    json=[]
)

print("Status:", r.status_code)
print(r.text[:500])
