from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://braucheklima.de/", wait_until="networkidle")

    inputs = page.locator("input")

    print("Anzahl Inputs:", inputs.count())

    for i in range(min(inputs.count(), 20)):
        try:
            print("-----")
            print("Index:", i)
            print("placeholder:", inputs.nth(i).get_attribute("placeholder"))
            print("type:", inputs.nth(i).get_attribute("type"))
            print("name:", inputs.nth(i).get_attribute("name"))
        except:
            pass

    browser.close()
