from selene import browser, be, have, by


class CheckPage:
    def __init__(self):
        self.browser = browser
        pass

    def open(self):
        browser.open("/")
        return self

    def should_have_menu_links(self):
        texts = [
            "Все рецепты",
            "Свежие рецепты",
            "Салаты",
            "Закуски",
            "Десерты",
            "Соусы",
            "Выпечка",
            "Бульоны и супы",
            "Горячие блюда"
        ]
        for text in texts:
            browser.element(by.text(text)).should(be.present)
        return self

    def should_have_site_name(self, name):
        browser.element(".logo").should(have.exact_text(name)).click()
        return self

    def open_login_page(self):
        browser.element(by.text("Войти на сайт")).click()
        return self

    def should_be_on_login_page(self):
        browser.should(have.url_containing("/login"))
        return self

    def get_links(self, **expected_urls):
        mapping = {
            "Все рецепты": "all_recipe_landing",
            "Свежие рецепты": "fresh_recipe_landing",
            "Бульоны и супы": "soup_landing",
            "Вторые блюда": "second_dish_landing",
            "Соусы": "souce_landing",
            "Закуски": "appetizer_landing",
            "Десерты": "deserts_landing",
            "Салаты": "salads_landing",
            "Выпечка": "bakers_landing",
        }
        for link_text, key in mapping.items():
            element = browser.element(by.text(link_text)).should(be.present)

            actual_href = element.get_attribute("href")
            expected = expected_urls.get(key)
            assert actual_href == expected, (
                f"Для ссылки '{link_text}' ожидался URL:\n{expected}\n"
                f"Получен: {actual_href}"
            )
        return self


app = CheckPage()
