from playwright.sync_api import sync_playwright


def test() -> None:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.commboost.ru/login")

        page.click("button._button_2wmor_35")

        assert page.locator("div._modal_content_vsmmv_12").is_visible()

        page.wait_for_timeout(3000)
        browser.close()


if __name__ == '__main__':
    test()
