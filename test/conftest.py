import pytest
from selene import browser
import os

from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://auth.lenzaos.com/'
    browser.config.window_width = os.getenv('window_width', '1900')
    browser.config.window_height = os.getenv('window_height', '1400')
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options


    yield
    browser.quit()


