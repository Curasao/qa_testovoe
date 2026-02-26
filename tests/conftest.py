import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setup_browser_landing():
    browser.config.base_url = "https://www.povarenok.ru"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-background-networking')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Реалистичный User-Agent
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")

    # Отключаем GPU (если возникают ошибки)
    options.add_argument("--disable-gpu")

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '127.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(f'https://user1:1234@selenoid.autotests.cloud/wd/hub',
                                             options=options)
    yield browser

    browser.quit()
