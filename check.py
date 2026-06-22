import requests

TOPIC = "porty"

data = requests.post(
    "https://braucheklima.de/api/availability",
    json=[]
).json()

treffer = []

for store in data:
    try:
        portasplit = store["articles"].get("Midea Portasplit")

        if not portasplit:
            continue

        stock = portasplit["stocks"][0]["stock"]

        if stock > 0:
            name = store["name"]
            city = store["city"]
            price = portasplit["prices"][0]["price"]
            url = portasplit["url"]

            treffer.append(
                f"📍 {name} ({city})\n"
                f"💰 {price} €\n"
                f"📦 Bestand: {stock}\n"
                f"🔗 {url}"
            )

    except Exception:
        pass

if treffer:
    message = "🚨 PortaSplit verfügbar!\n\n" + "\n\n".join(treffer[:10])

    requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers={"Title": "PortaSplit Alarm"}
    )

    print("Nachricht gesendet")
else:
    print("Keine Verfügbarkeit gefunden")
