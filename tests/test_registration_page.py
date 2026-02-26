import pytest
from selene import browser, be, have, by


class RegistrationPage:

    def __init__(self):
        self.browser = browser
        pass

def test_login_user_valid_data():
        login_valid = 'bellkapd-2026@yandex.ru'
        pwd_valid = 'testoviy2026'
        browser.element('#tl_login_id').press_enter()
        browser.element('input[placeholder*="Ваш e-mail или имя"]').should(be.visible).set_value(
            login_valid).press_enter()
        browser.element('input[placeholder*="Пароль"]').should(be.visible).set_value(pwd_valid).press_enter()

def test_login_user_unvalid_data():
        login_unvalid = 'test2026@yandex.ru'
        pwd_unvalid = 'test2026'
        browser.element('#tl_login_id').press_enter()
        browser.element('input[placeholder*="Ваш e-mail или имя"]').should(be.visible).set_value(login_unvalid)
        browser.element('input[placeholder*="Пароль"]').should(be.visible).set_value(pwd_unvalid).press_enter()


