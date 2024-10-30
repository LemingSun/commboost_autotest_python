def test_successful_login(page, data, urls):
    # Вводим валидные данные
    page.fill("input[name='email']", data["email"])
    page.fill("input[name='password']", data["password"])

    # Нажимаем кнопку "Войти"
    page.click("button[type='submit']")

    # Ожидание успешного перехода
    page.wait_for_url(urls["personalAccount"])
    assert page.url == urls["personalAccount"], (f"Не удалось авторизоваться на странице {urls['loginPage']} с логином "
                                                 f"{data['email']} и паролем {data['password']}")


def test_disable_button_submit_with_miss_email(page, data):
    # Вводим пустой логин и валидный пароль
    page.fill("input[name='email']", '')
    page.fill("input[name='password']", data["password"])

    # Проверяем кнопку "Войти"
    assert page.get_by_role('button', disabled=True, name='submit'), "Кнопка Войти активна пр попытке входа без email"


def test_disable_button_submit_with_incorrect_email_format(page, data):
    # Вводим логин не правильного формата и валидный пароль
    page.fill("input[name='email']", data["incorrectEmailFormat"])
    page.fill("input[name='password']", data["password"])

    # Проверяем кнопку "Войти"
    assert page.get_by_role('button', disabled=True, name='submit'), ("Кнопка Войти активна при вводе email не "
                                                                      "правильного формата")


def test_alert_message_if_incorrect_email_format(page, data, alertContent):
    # Вводим логин не правильного формата и валидный пароль
    page.fill("input[name='email']", data["incorrectEmailFormat"])
    page.fill("input[name='password']", data["password"])

    # Ловим алерт о неверном формате почты
    page.wait_for_selector("._container_197er_2")

    # Проверяем текст алерта
    assert (page.locator('._container_197er_2').text_content() ==
            alertContent["incorrectEmailFormat"]), ("Сообщение о не верном формате email не отображается или не "
                                                    "правильное.")


def test_disable_button_submit_with_miss_password(page, data):
    # Вводим валидный логин и пустой пароль
    page.fill("input[name='email']", data["email"])
    page.fill("input[name='password']", "")

    # Проверяем кнопку "Войти"
    assert page.get_by_role('button', disabled=True, name='submit')


def test_disable_button_submit_with_short_password(page, data):
    # Вводим валидный логин и пароль не допустимой длины
    page.fill("input[name='email']", data["email"])
    page.fill("input[name='password']", data["tooShortPassword"])

    # Проверяем кнопку "Войти"
    assert page.get_by_role('button', disabled=True, name='submit'), ("Кнопка Войти активна при пароле, меньше "
                                                                      "необходимой длинны")


def test_alert_message_if_short_password(page, data, alertContent):
    # Вводим валидный логин и пароль не допустимой длины
    page.fill("input[name='email']", data["email"])
    page.fill("input[name='password']", data["tooShortPassword"])

    # Убираем указатель с поля пароля
    page.click("input[name='email']")

    # Ловим алерт о неверном формате почты
    page.wait_for_selector("._container_197er_2")

    # Проверяем текст алерта
    assert (page.locator('._container_197er_2').text_content() ==
            alertContent["shortPassword"]), ("Сообщение о слишком коротком пароле не появляется или имеет не верный "
                                             "формат.")


def test_fault_login_with_invalid_email(page, data, urls):
    # Вводим не валидный логин и валидный пароль
    page.fill('input[name="email"]', data["notValidEmail"])
    page.fill('input[name="password"]', data["password"])

    # Нажимаем на кнопку входа
    page.click('button[type="submit"]')

    # Проверка что не зашло в лк
    page.wait_for_timeout(1000)  # Ожидание
    assert page.url != urls["personalAccount"], "Вход в систему произведен с не валидным email"


def test_alert_massage_invalid_email(page, data, alertContent):
    # Вводим не валидный логин и валидный пароль
    page.fill('input[name="email"]', data["notValidEmail"])
    page.fill('input[name="password"]', data["password"])

    # Нажимаем на кнопку входа
    page.click('button[type="submit"]')

    # Ждем появления алерта
    page.wait_for_selector('._container_197er_2')

    # Проверяем текст алерта
    alert_text = page.inner_text('._container_197er_2')
    assert alert_text == alertContent["incorrectLoginOrPassword"], ("Сообщение о не валидном email не появляется или "
                                                                    "имеет не верный формат.")


def test_fault_login_with_invalid_password(page, data, urls):
    # Вводим валидный логин и не валидный пароль
    page.fill('input[name="email"]', data["email"])
    page.fill('input[name="password"]', data["notValidPassword"])

    # Нажимаем на кнопку входа
    page.click('button[type="submit"]')

    # Проверка что не зашло в лк
    page.wait_for_timeout(1000)  # Ожидание
    assert page.url != urls["personalAccount"], "Вход в систему произведен с не валидным паролем"


def test_alert_massage_invalid_password(page, data, alertContent):
        # Вводим валидный логин и не валидный пароль
    page.fill('input[name="email"]', data["email"])
    page.fill('input[name="password"]', data["notValidPassword"])

    # Нажимаем на кнопку входа
    page.click('button[type="submit"]')

    # Ждем появления алерта
    page.wait_for_selector('._container_197er_2')

    # Проверяем текст алерта
    alert_text = page.inner_text('._container_197er_2')
    assert alert_text == alertContent["incorrectLoginOrPassword"], ("Сообщение о не валидном пароле не появляется или "
                                                                    "имеет не верный формат.")


def test_block_bruteforce():
    pass
