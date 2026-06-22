from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://braucheklima.de/", wait_until="networkidle")

    ort = page.locator("input").nth(1)

    ort.fill("Frankfurt am Main")

    page.wait_for_timeout(2000)

    print("Buttons:")
    print(page.locator("button").count())

    for i in range(min(page.locator("button").count(), 20)):
        try:
            print(i, page.locator("button").nth(i).inner_text())
        except:
            pass

    browser.close()
