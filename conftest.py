import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture(scope="function")
def page(page: Page):
    # Переходим на страницу авторизации
    page.goto("https://demo.commboost.ru/login")

    page.evaluate("document.querySelector('input[name=\"email\"]').removeAttribute('readonly');")
    page.evaluate("document.querySelector('input[name=\"password\"]').removeAttribute('readonly');")

    yield page


@pytest.fixture()
def data():
    return {
        "email": "demo@example.com",
        "password": "123321",
        "incorrectEmailFormat": "demo_example.com",
        "tooShortPassword": "123",
        "notValidEmail": "demo@example.ru",
        "notValidPassword": "123456",
            }


@pytest.fixture()
def urls():
    home = "https://demo.commboost.ru/"
    return {
        "loginPage": f"{home}login",
        "personalAccount": f"{home}account",
    }


@pytest.fixture()
def alertContent():
    return {
        "incorrectEmailFormat": "Неверный формат почты",
        "shortPassword": "Пароль должен быть не менее 6 символов",
        "incorrectLoginOrPassword": "Неверный логин или пароль",
    }
