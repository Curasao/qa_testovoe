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

    yield browser

    browser.quit()
