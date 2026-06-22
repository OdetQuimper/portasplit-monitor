import requests

TOPIC = "porty"

# Testnachricht senden
requests.post(
    f"https://ntfy.sh/{TOPIC}",
    data="GitHub-Überwachung erfolgreich eingerichtet!".encode("utf-8"),
    headers={"Title": "PortaSplit Monitor"}
)

print("Nachricht gesendet")
