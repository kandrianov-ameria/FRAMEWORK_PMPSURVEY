import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from .locator import assert_success
from .locators import HomePageSelectors as HPS


class HomePage(BasePage):



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = HPS.homepage_url
        self.go()
        self.implicitly_wait(5)
        self.maximize()


    # Find and return the strating country pop-up elements 

    @property
    def country_popup(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HPS.country_popup_css)
        return BaseElement(self.browser, locator)

    @property
    def popup_img(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HPS.country_popup_img_css)
        return BaseElement(self.browser, locator)

    @property
    def popup_title(self):
        locator = Locator(by=By.XPATH, value=HPS.country_popup_title_xpath)
        return BaseElement(self.browser, locator)

    @property
    def popup_select(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HPS.country_popup_select_css)
        return BaseElement(self.browser, locator)

    @property
    def popup_close(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HPS.country_popup_close_css)
        return BaseElement(self.browser, locator)

    @property
    def fake_element(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HPS.fake_button)
        return BaseElement(self.browser, locator)

    #Country select options:
    @property
    def takepart_btn(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HPS.home_page_takepart_btn_css)
        return BaseElement(self.browser, locator)





