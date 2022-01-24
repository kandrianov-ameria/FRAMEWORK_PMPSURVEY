import pytest
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .pages.locators import HomePageSelectors as HPS
from .pages.home_page import HomePage
from .pages.locator import assert_success
from time import sleep



 # will need 2 separate tests:
    # 1 - open home url -> close popup -> there is the home page (find the participate button)
    # 2 - openhome url -> select country -> proceed btn (later there will be an api request) -> find the particiapate button 


# Two Test Classes: 
# 1. StartPopupTests (all elements present, neg test -> close, pos test -> proceed) how to parametrize?, 
# 2. HomePageTests 

@pytest.fixture(scope='module')
def page(browser):
    return HomePage(browser)

    # return page



def test_page_opens(page):
    currentlink = page.get_window_url()
    assert currentlink == page.url and assert_success(f'Url is {page.url}!'), "Links don't match." 

@pytest.mark.parametrize('element_name', ['country_popup', 'popup_img', 'popup_title', 'popup_select', 'popup_close'])
def test_01_that_elements_ispresent(page, element_name):
    # page = HomePage(browser)
    element = page.country_popup
    assert element.find() and assert_success(f'Element is present'), f"No such element: {element}."
    sleep(1)

@pytest.mark.xfail
def test_fake_elements_ispresent():
    # page = HomePage(browser)
    element = page.fake_element
    assert element.find() and assert_success(f'Xfail - No fake element is present'), f"Fake element is present: {element}?"


# pytest -s -v --browser_name=chrome test_home_page.py
# pytest -s -v --browser_name=firefox test_home_page.py
# pytest -s -v --browser_name=edge test_home_page.py

