from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC




class BaseElement(object):
    def __init__(self, browser, locator):
        self.browser = browser
        self.locator = locator
        self.web_element = None

    # Look for the on the DOM. 

    def find(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return True

    # Check if the element is visible.

    def is_visible(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return True

    # Check if the element is present in the DOM



    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None

    def dropdown_select(self):
        element = WebDriverWait(self.browser, 10).until(
        EC.element_located_to_be_selected(locator=self.locator)
        )
        self.web_element = element
        return Select(element)
        

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute
    
    @property
    def text(self):
        text = self.web_element.text
        return text


