import requests

data = requests.post(
    "https://braucheklima.de/api/availability",
    json=[]
).json()

print("Anzahl Filialen:", len(data))

for store in data[:5]:
    print(store["name"])
