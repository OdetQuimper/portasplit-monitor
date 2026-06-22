from playwright.sync_api import sync_playwright
import requests

TOPIC = "porty"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://braucheklima.de/", wait_until="networkidle")

    text = page.locator("body").inner_text()

    if "mit PortaSplit\n0" not in text:
        requests.post(
            f"https://ntfy.sh/{TOPIC}",
            data="🚨 Es gibt aktuell PortaSplit-Filialen!".encode("utf-8"),
            headers={"Title": "PortaSplit Alarm"}
        )

    browser.close()

print("Fertig")
