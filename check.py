from playwright.sync_api import sync_playwright
import requests

TOPIC = "porty"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://braucheklima.de/", wait_until="networkidle")

    text = page.locator("body").inner_text()

    if "Verfügbar" in text:
        requests.post(
            f"https://ntfy.sh/{TOPIC}",
            data="Test: Das Wort 'Verfügbar' wurde auf der Seite gefunden.".encode("utf-8"),
            headers={"Title": "PortaSplit Test"}
        )

    browser.close()

print("OMID TEST 12345")
