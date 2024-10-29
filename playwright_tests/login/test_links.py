def test_link_telegramm_bot(page, urls):
    # Прожимаем ссылку на телеграмм бота
    with page.expect_popup() as page_info:
        page.get_by_role("link").first.click()

    # Присваиваем значение новому обьекту страницы
    pageTelegramm = page_info.value

    # Проверяем правильный урл страницы
    assert pageTelegramm.url == urls["telegrammBot"]


def test_link_whatsap_bot(page, urls):
    # Прожимаем ссылку на вотсап бота
    with page.expect_popup() as page_info:
        page.get_by_role("link").nth(1).click()

    # Присваиваем значение новому обьекту страницы
    pageWhatsapp = page_info.value

    # Проверяем правильный урл страницы
    assert pageWhatsapp.url == urls["whatsapBot"]


def test_email_feedback():
    pass


def test_button_put_request(page):
    # Прожимаем кнопку "Оставить заявку"
    page.get_by_role("button", name="Оставить заявку").click()

    # Проверяем появление окна с заявкой
    assert page.locator("div._modal_content_vsmmv_12").is_visible()

def test_day_night_mode():
    pass
