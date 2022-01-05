import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome, firefox or edge')


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        options = Options()
        print(f"\nStarting {browser_name} browser for testing ...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        print(f"\nStarting browser for testing {version_lang} version...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"Browser {version_lang} still is not implemented")
    yield browser
    print("\nQuitting browser...")
    browser.quit()
