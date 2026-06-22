import requests
import math

TOPIC = "porty"

FRANKFURT_LAT = 50.1109
FRANKFURT_LON = 8.6821


def distance_km(lat1, lon1, lat2, lon2):
    r = 6371

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    return r * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


data = requests.post(
    "https://braucheklima.de/api/availability",
    json=[]
).json()

treffer = []

for store in data:

    try:
        if not store["lat"] or not store["lon"]:
            continue

        entfernung = distance_km(
            FRANKFURT_LAT,
            FRANKFURT_LON,
            store["lat"],
            store["lon"]
        )

        if entfernung > 100:
            continue

        portasplit = store["articles"].get("Midea Portasplit")

        if not portasplit:
            continue

        stock = portasplit["stocks"][0]["stock"]

        if stock <= 0:
            continue

        price = portasplit["prices"][0]["price"]

        treffer.append(
            f"{store['name']} | "
            f"{round(entfernung)} km | "
            f"{price} € | "
            f"Bestand {stock}"
        )

    except Exception:
        pass

print("Treffer:")

for t in treffer:
    print(t)
