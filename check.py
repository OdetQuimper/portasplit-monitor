from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://braucheklima.de/", wait_until="networkidle")

    ort = page.locator("input").nth(1)

    ort.fill("Frankfurt am Main")

    page.wait_for_timeout(3000)

    print(page.locator("body").inner_text()[:3000])

    browser.close()
