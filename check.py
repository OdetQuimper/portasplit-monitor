from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://braucheklima.de/", wait_until="networkidle")

    print("Seite geladen")

    print(page.locator("text=Nur Verfügbare").count())
    print(page.locator("text=Portasplit Cool").count())

    browser.close()
