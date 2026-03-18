from asyncio import timeout
from selene import browser, have, be,command
import pytest
import allure


class AuthPage:
    def open(self):
        browser.open('https://www.povarenok.ru')

    def fill_login(self):
        browser.element('#tl_login_id').should(be.visible).type('bellkapd-2026')


    def fill_password(self):
        browser.element('#tl_pwd_id').should(be.visible).type('testoviy2026')


    def fill_mediafort_login(self):
        browser.driver.execute_script(
            "document.querySelector('#login_id').value = 'bellkapd-2026'"
        )

    def fill_mediafort_pwd(self):
        browser.driver.execute_script(
            "document.querySelector('#password_id').value = 'testoviy2026'"
        )


    def fill_mediafort_unsucces_pwd(self):
        browser.driver.execute_script(
            "document.querySelector('#password_id').value = 'test_2026'"
        )

    def fill_mediafort_unsuccess_login(self):
        browser.driver.execute_script(
            "document.querySelector('#login_id').value = 'test-2026'"
        )

    def press_button(self):
        browser.driver.execute_script(
            "document.querySelector('input[value=\"Войти на сайт\"]').click()"
        )



    def add_recipe(self):
        browser.element('.sbm-link').should(be.visible).click()

    def fill_rek_login(self):
        browser.element('.table>tbody>tr>td>input[placeholder="Ваше имя"]').should(be.visible).with_(timeout=30).type('1111')

    def fill_rek_email(self):
        browser.element('.table>tbody>tr>td>input[placeholder="Ваш e-mail"]').should(be.visible).with_(timeout=30).type('test@yandex.ru')

    def submit_button(self):
        browser.element('input[value="Войти!"]').should(be.visible).click()

    def check_success(self):

        browser.element('.userhello').should(
                have.text('Здравствуйте, bellkapd-2026')
            )

    def check_failure(self):
        browser.element('.main-form').should(
            have.text('Пользователь с таким именем не найден, либо указан неправильный пароль. Если вы входите на этот сайт впервые, введите e-mail вместо никнейма.')
        )


@allure.title('Авторизация с корректными данными')
def test_valid_login(setup_browser_landing):
    auth_page = AuthPage()
    auth_page.open()
    auth_page.press_button()
    auth_page.fill_mediafort_login()
    auth_page.fill_mediafort_pwd()
    auth_page.submit_button()
    auth_page.check_success()


@allure.title('Авторизация с некорректными данными')
def test_invalid_login(setup_browser_landing):
    auth_page = AuthPage()
    auth_page.open()
    auth_page.press_button()
    auth_page.fill_mediafort_unsuccess_login()
    auth_page.fill_mediafort_unsucces_pwd()
    auth_page.submit_button()
    auth_page.check_failure()


