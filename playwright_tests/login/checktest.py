from playwright.sync_api import sync_playwright


def test() -> None:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.commboost.ru/login")

        page.locator("div._toggleSwitch_fdixj_33").click()
        # page.locator("div").filter(has_text=re.compile(r"^CommBoostОставить заявку$")).locator("div").nth(2).click()
        page.wait_for_timeout(1000)

        page.locator("div._toggleSwitch_fdixj_33").click()
        print(page.eval_on_selector("html", "element => element.getAttribute('style')"))

        page.wait_for_timeout(3000)
        browser.close()


if __name__ == '__main__':
    test()
