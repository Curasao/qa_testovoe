from asyncio import timeout
from selene import browser, have, be
import pytest
import allure


class AuthPage:
    def __init__(self):
        self.login_field = browser.element('#tl_login_id')
        self.password_field = browser.element('#tl_pwd_id')
        self.submit_button = browser.element('[value="Войти на сайт"]')

    def open(self, setup_browser_landing):
        browser.open('https://www.povarenok.ru')

    def fill_login(self, email_or_username, setup_browser_landing):
        browser.element(self.login_field).type('bellkapd-2026')

    def fill_password(self, password, setup_browser_landing):
        browser.element(self.password_field).type('testoviy-2026')

    def submit_auth(self):
        browser.element(self.submit_button).click()

    def check_success(self):
        browser.element('b').should(have.text('Здравствуйте, bellkapd-2026'))

    def check_failure(self):
        browser.element('b').should(have.text('Если вы входите на этот сайт впервые, введите e-mail вместо никнейма.'))


@allure.title('Авторизация с корректными данными')
def test_valid_login():
    auth_page = AuthPage()
    auth_page.open()
    browser.element('.dr__cross').with_(timeout=30).should(be.visible).click()
    auth_page.fill_login('bellkapd-2026@yandex.ru')
    auth_page.fill_password('testoviy2026')
    auth_page.submit_auth()
    auth_page.check_success()


@allure.title('Авторизация с некорректными данными')
def test_invalid_login():
    auth_page = AuthPage()
    auth_page.open()
    browser.element('.dr__cross').with_(timeout=30).should(be.visible).click()
    auth_page.fill_login('bad_email@example.com')
    auth_page.fill_password('incorrect_pass')
    auth_page.submit_auth()
    auth_page.check_failure()
