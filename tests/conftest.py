import os

import pytest
from dotenv import load_dotenv

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

DEFAULT_BROWSER_VERSION = '128.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION,
        help='browser version (firefox: 128.0, 127.0)'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def get_option_browser_version(request):
    return request.config.getoption('--browser_version')


@pytest.fixture(scope='session')
def setup_browser(get_option_browser_version):
    browser_version = get_option_browser_version
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
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
def open_homepage(setup_browser):
    browser.open('/')

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
