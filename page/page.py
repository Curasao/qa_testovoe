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


app = CheckPage()
