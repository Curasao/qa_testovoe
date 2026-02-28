import pytest
from selene import browser, be, have, by
import time

class RegistrationPage:

    def __init__(self):
        self.browser = browser
        pass


def test_login_user_valid_data():
    browser.element('#tl_login_id').should(be.blank).press_enter()
    time.sleep(10)
    browser.element('.dr__cross').should(be.visible).click()
    browser.element('#login_id').should(be.enabled).type('bellkapd-2026@yandex.ru').click()
    time.sleep(10)
    browser.element('#password_id').should(be.enabled).type('testoviy2026').click()


def test_login_user_unvalid_data():
    browser.element('#tl_login_id').should(be.blank).press_enter()
    time.sleep(10)
    browser.element('.dr__cross').should(be.visible).click()
    browser.element('#login_id').should(be.enabled).type('b@yandex.ru').click()
    time.sleep(10)
    browser.element('#password_id').should(be.enabled).type('test1111').click()
