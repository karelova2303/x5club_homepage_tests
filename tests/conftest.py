import os

import pytest
from dotenv import load_dotenv

from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

DEFAULT_BROWSER_VERSION = '125.0'

def pytest_addoption(parser):
    parser.addoption('--browser_version', default='125.0')

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='session')
def open_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
            'browserName': 'firefox',
            'browserVersion': browser_version,
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True,
                'screenResolution': '1920x1080x24'
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_pass = os.getenv('SELENOID_PASS')
    selenoid_url = os.getenv('SELENOID_URL')

    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options
    )

    browser.config.driver = driver

    browser.config.base_url = 'https://x5club.ru'
    browser.driver.maximize_window()

    yield

    browser.quit()


@pytest.fixture(scope='function')
def open_homepage(open_browser):
    browser.open('/')

    yield browser

    attach.add_screenshot(browser)
    # attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
