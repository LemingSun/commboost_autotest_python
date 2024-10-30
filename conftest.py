import pytest
from playwright.sync_api import Page

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
        "telegrammBot": "https://t.me/commboost",
        "whatsapBot": "https://api.whatsapp.com/send/?phone=79956595051&text&type=phone_number&app_absent=0",
    }


@pytest.fixture()
def alertContent():
    return {
        "incorrectEmailFormat": "Неверный формат почты",
        "shortPassword": "Пароль должен быть не менее 6 символов",
        "incorrectLoginOrPassword": "Неверный логин или пароль",
    }


@pytest.fixture()
def dayNightModeContent():
    return {
        "dayMode": "--primary-color: #FFFFFF; --secondary-color: #F2F5F7; --third-color: #123347;"
                   " --text-primary-color: #1C2434; --text-secondary-color: #F2F5F7; --accent-color: #8FA6B2;"
                   " --addition-color: #D1DADF; --shadow-color: #CADAE4; --default-button-color: #123347;"
                   " --inverse-button-border-color: #123347; --soundbar-background-color: #D2D2D2;"
                   " --soundbar-progress-color: #123347;",
        "nightMode": "--primary-color: #123347; --secondary-color: #0F2B3C; --third-color: #091E2b;"
                     " --text-primary-color: #F2F5F7; --text-secondary-color: #8FA6B2; --accent-color: #517285;"
                     " --addition-color: #BDD2F3; --shadow-color: rgba(0, 0, 0, 0.33); --default-button-color: #8FA6B2;"
                     " --inverse-button-border-color: #8FA6B2; --soundbar-background-color: #F2F5F7;"
                     " --soundbar-progress-color: #8FA6B2;",
    }
