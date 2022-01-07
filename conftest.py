import pytest
from selenium import webdriver
from .cfg_drivers import driverpath
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager




def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome, firefox or edge in the command line like so " --browser_name=chrome"')


# @pytest.fixture(scope='module')
# def browser(request):
#     browser_name = request.config.getoption('browser_name')
#     if browser_name == "chrome":
#         # options = Options()
#         print(f"\nStarting {browser_name} browser for testing ...")
#         browser = webdriver.Chrome(ChromeDriverManager().install())
#     elif browser_name == "firefox":
#         print(f"\nStarting {browser_name} browser for testing ...")
#         browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#     elif browser_name == "edge":
#         print(f"\nStarting {browser_name} browser for testing ...")
#         browser = webdriver.Edge(EdgeChromiumDriverManager().install())
#     else:
#         print(f'Choose browser: chrome, firefox or edge in the command line like so " --browser_name=chrome"')
#     yield browser
#     print("\nQuitting browser...")
#     browser.quit()


@pytest.fixture(scope='module')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        # options = Options()
        print(f"\nStarting {browser_name} browser for testing ...")
        browser = webdriver.Chrome(executable_path=driverpath.get_Chrome_driver_location())
    elif browser_name == "firefox":
        print(f"\nStarting {browser_name} browser for testing ...")
        browser = webdriver.Firefox(executable_path=driverpath.get_Firefox_driver_location())

    elif browser_name == "edge":
        print(f"\nStarting {browser_name} browser for testing ...")
        browser = webdriver.Edge(executable_path=driverpath.get_Edge_driver_location())
    else:
        print(f'Choose browser: chrome, firefox or edge in the command line like so " --browser_name=chrome"')
    yield browser
    print("\nQuitting browser...")
    browser.quit()

