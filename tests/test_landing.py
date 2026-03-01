
import allure
from page.page import app
from page.page import CheckPage
from selene import browser, be, have, by

@allure.epic('Главная страница')
@allure.feature('Проверка работы главной страницы')
@allure.title('Проверка отображения меню')



@allure.title('Проверка названия сайта')
def test_site_name_povarenok(setup_browser_landing):
    app = CheckPage()
    app.open()
    app.should_have_site_name('Поваренок')


@allure.title('Проверка ссылки Все рецепты')
def test_link_all_recipes(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/'))

@allure.title('Проверка ссылки Свежие рецепты')
def test_link_new_recipes(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/?sort=newest"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/?sort=newest'))

@allure.title('Проверка ссылки Бульоны и супы')
def test_link_soups(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/category/2/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/category/2/'))

@allure.title('Проверка ссылки Горячие блюда')
def test_link_hot_dishes(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/category/6/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/category/6/'))

@allure.title('Проверка ссылки Соусы')
def test_link_sauces(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/category/23/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/category/23/'))

@allure.title('Проверка ссылки Закуски')
def test_link_snacks(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/category/15/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/category/15/'))

@allure.title('Проверка ссылки Десерты')
def test_link_desserts(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/category/30/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/category/30/'))

@allure.title('Проверка ссылки Салаты')
def test_link_salads(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/category/12/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/category/12/'))

@allure.title('Проверка ссылки Выпечка')
def test_link_baking(setup_browser_landing):
    app = CheckPage()
    app.open()
    link_element = browser.element('a[href="https://www.povarenok.ru/recipes/category/25/"]')
    link_element.should(have.attribute('href', 'https://www.povarenok.ru/recipes/category/25/'))