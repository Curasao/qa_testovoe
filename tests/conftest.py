import pytest
from selene import browser, have, be
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setup_browser_landing():
      options = Options()
      options.headless = True
      driver = webdriver.Chrome(options=options)
      driver.set_window_size(1920, 1080)
      browser.config.driver = driver
      browser.config.base_url = "https://www.povarenok.ru"
      browser.config.timeout = 30

      yield browser

      browser.quit()
