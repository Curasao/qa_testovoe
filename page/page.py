from selene import browser, be, have, by


class CheckPage:

    def open(self):
        browser.open("/")
        return self

    def close_popup(self):
        popup = browser.element('.dr__cross')

        if popup.matching(be.visible):
            popup.click()

        return self

    def should_have_site_name(self, name):
        browser.element(".logo").should(have.text(name))

        return self

    def should_have_menu_link(self, text, href):
        link = browser.all('.recipes-nav a').element_by(have.text(text))
        link.should(be.visible)
        link.should(have.attribute('href').value_containing(href))

    def landing_search(self):
        browser.element('[placeholder*="Поиск"]').should(be.visible).type('грибной суп').press_enter()


app = CheckPage()
