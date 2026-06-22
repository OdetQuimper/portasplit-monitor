import requests
import math

TOPIC = "porty"

FRANKFURT_LAT = 50.1109
FRANKFURT_LON = 8.6821
RADIUS_KM = 100


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
ids = []

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

        if entfernung > RADIUS_KM:
            continue

        portasplit = store["articles"].get("Midea Portasplit")

        if not portasplit:
            continue

        stock = portasplit["stocks"][0]["stock"]

        if stock <= 0:
            continue

        price = portasplit["prices"][0]["price"]
        url = portasplit["url"]

        ids.append(store["name"])

        treffer.append(
            f"📍 {store['name']}\n"
            f"📏 {round(entfernung)} km\n"
            f"💰 {price} €\n"
            f"📦 Bestand: {stock}\n"
            f"🔗 {url}"
        )

    except Exception as e:
        print("Fehler:", e)

current_state = "|".join(sorted(ids))

print("current_state:")
print(current_state)
print("Anzahl IDs:", len(ids))

try:
    with open("last_alert.txt", "r", encoding="utf-8") as f:
        old_state = f.read().strip()
except:
    old_state = ""

print("old_state:")
print(old_state)

if current_state and current_state != old_state:

    message = "🚨 PortaSplit verfügbar!\n\n" + "\n\n".join(treffer)

    requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers={"Title": "PortaSplit Alarm"}
    )

    with open("last_alert.txt", "w", encoding="utf-8") as f:
        f.write(current_state)

    with open("last_alert.txt", "r", encoding="utf-8") as f:
        print("Dateiinhalt nach Schreiben:")
        print(f.read())

    print("Neue Treffer gemeldet")

else:
    print("Keine Änderung")
