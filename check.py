from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://braucheklima.de/", wait_until="networkidle")

    print("Links:")
    links = page.locator("button, a")

    for i in range(min(200, links.count())):
        try:
            text = links.nth(i).inner_text().strip()
            if text in ["10 km", "25 km", "50 km", "100 km", "200 km"]:
                print(text)
        except:
            pass

    browser.close()
