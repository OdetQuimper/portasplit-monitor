import requests

data = requests.post(
    "https://braucheklima.de/api/availability",
    json=[]
).json()

for store in data:
    if store["name"] == "Hornbach Berlin-Marzahn":
        portasplit = store["articles"].get("Midea Portasplit")

        print("Filiale:", store["name"])
        print("Stadt:", store["city"])

        print("Bestand:",
              portasplit["stocks"][0]["stock"])

        print("Preis:",
              portasplit["prices"][0]["price"])

        print("Link:",
              portasplit["url"])

        break
