import pytest
from selene import browser, be, have, by
import time

class RegistrationPage:

    def __init__(self):
        self.browser = browser
        pass

def test_login_user_valid_data():
        login_valid = 'bellkapd-2026@yandex.ru'
        pwd_valid = 'testoviy2026'
        browser.element('#tl_login_id').should(be.blank).press_enter()
        time.sleep(10)
        browser.element('#login_id').should(be.enabled).set_value(login_valid).click()
        time.sleep(10)
        browser.element('#password_id').should(be.enabled).set_value(pwd_valid).click()



