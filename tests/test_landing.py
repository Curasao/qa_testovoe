import allure
import pytest
from page.page import CheckPage


@allure.epic('Главная страница')
@allure.feature('Проверка работы главной страницы')


@allure.title('Проверка названия сайта')
def test_site_name_povarenok(setup_browser_landing):
    app = CheckPage()
    app.open()
    app.should_have_site_name('Поваренок')


@allure.title('Проверка ссылки Все рецепты')
def test_link_all_recipes(setup_browser_landing):
    app = CheckPage()
    app.open()
    app.should_have_menu_link('Все рецепты', '/recipes/cat/')



@allure.title('Проверка ссылок категорий')
@pytest.mark.parametrize("name, href", [
    ('Свежие рецепты', '/recipes'),
    ('Бульоны и супы', '/recipes/category/2/'),
    ('Горячие блюда', '/recipes/category/6/'),
    ('Соусы', '/recipes/category/23/'),
    ('Закуски', '/recipes/category/15/'),
    ('Десерты', '/recipes/category/30/'),
    ('Салаты', '/recipes/category/12/'),
    ('Выпечка', '/recipes/category/25/'),
])
def test_recipe_links(setup_browser_landing, name, href):
    app = CheckPage()
    app.open()
    app.should_have_menu_link(name, href)


@allure.title('Проверка поиска на странице')
def test_search(setup_browser_landing):
    app = CheckPage()
    app.open()
    app.landing_search()