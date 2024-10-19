from playwright.sync_api import sync_playwright


def test_fault_login_with_incorrect_email() -> None:
    with sync_playwright() as pw:
        # Создаем браузер и открываем страницу
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        # Переходим на страницу авторизации
        page.goto("https://demo.commboost.ru/login")

        # Удаляем аттрибуты readonly
        page.evaluate("document.querySelector('input[name=\"email\"]').removeAttribute('readonly');")
        page.evaluate("document.querySelector('input[name=\"password\"]').removeAttribute('readonly');")

        # Вводим валидный логин и пароль не правильного формата
        page.fill("input[name='email']", "demo@example.com")
        page.fill("input[name='password']", "12332")

        # Убираем указатель с поля пароля
        page.click("input[name='email']")

        # Ловим алерт о неверном формате почты
        page.wait_for_selector("._container_197er_2")

        print(page.locator('._container_197er_2').text_content())

        # Проверяем кнопку "Войти"
        assert page.get_by_role('button', disabled=True, name='submit')

        browser.close()


if __name__ == '__main__':
    test_fault_login_with_incorrect_email()
