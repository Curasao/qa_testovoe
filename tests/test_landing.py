from page.page import app
import time
from selene import be, have, by
import allure
from allure import step
from allure import epic, feature, suite,title

@allure.epic('Главная страница')
@allure.feature('Проверка работы главной страницы')
@allure.step('Проверка работы меню')
def test_submit_menu(setup_browser_landing):
    app.open()
    app.should_have_menu_links()

@allure.step('Проверка названия сайта')
def test_site_name_povarenok(setup_browser_landing):
    app.open()
    time.sleep(5)
    app.should_have_site_name('Поваренок.ру')



@allure.step('Проверка работы ссылок')
def test_check_links(setup_browser_landing):
    app.open()
    time.sleep(10)
    app.get_links(
        all_recipes='https://www.povarenok.ru/recipes/cat/',
        fresh_recipes_landing='https://www.povarenok.ru/recipes/',
        soup_landing='https://www.povarenok.ru/recipes/category/2/',
        second_dish_landing='https://www.povarenok.ru/recipes/category/6/',
        salads_landing='https://www.povarenok.ru/recipes/category/12/',
        appetizers_landing='https://www.povarenok.ru/recipes/category/15/',
        bakery_landing='https://www.povarenok.ru/recipes/category/25/',
        desserts_landing='https://www.povarenok.ru/recipes/category/30/',
        sauce_landing='https://www.povarenok.ru/recipes/category/23/'
    )


