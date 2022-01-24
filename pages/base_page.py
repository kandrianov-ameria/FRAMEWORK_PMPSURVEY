
from selenium.webdriver.support import expected_conditions as EC



class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        self.url = None
        
    def go(self):
        return self.browser.get(self.url)

    def maximize(self):
        return self.browser.maximize_window()

    def implicitly_wait(self, timeout: int):
         return self.browser.implicitly_wait(timeout)

    def get_window_url(self):
         return self.browser.current_url
         



    # def is_element_present(self, element, locator):
    #     element = BaseElement(element, locator)
    #     """The method to catch exceptions"""
    #     try:
    #         element.find()
    #     except NoSuchElementException:
    #         return False
    #     else:
    #         print("The element is present")
    #     return True

#     # NEGATIVE ELEMENT CHECKS

#     def is_not_element_present(self, locator, timeout=4):
#         """Check that an element is not shown on a page.
#         Using Selenium explicit waits"""
#         try:
#             WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return True
#         return False

#     def is_disappeared(self, how, what, timeout=4):
#         """Check that an element will disappear from a page.
#         Using Selenium explicit waits"""
#         try:
#             WebDriverWait(self.browser, timeout, 1, TimeoutException).\
#                 until_not(EC.presence_of_element_located((how, what)))
#         except TimeoutException:
#             return False
#         return True

# # QUIZ SOLVER

#     def solve_quiz_and_get_code(self):
#         alert = self.browser.switch_to.alert
#         x = alert.text.split(" ")[2]
#         answer = str(math.log(abs(12*math.sin(float(x)))))
#         alert.send_keys(answer)
#         alert.accept()
#         try:
#             alert = self.browser.switch_to.alert
#             alert_text = alert.text
#             print(f"Your code: {alert_text}")
#             alert.accept()
#         except NoAlertPresentException:
#             print("No second alert presented")

# # GO TO LOGIN PAGE

#     def go_to_login_page(self):
#         """The method to check that a guest can go to login page."""

#         link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
#         link.click()
#         # return LoginPage(browser=self.browser, url=self.browser.current_url)

#     def should_be_login_link(self):
#         """The method checks that there is a login page link on the Main page."""

#         assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

#     def should_be_authorised_user(self):
#         assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, " \
#                                                                      "probably the user is unauthorized"


# # GO TO BASKET PAGE

#     def go_to_basket_page(self):
#         """The method to check that a guest can go to the basket page."""

#         link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
#         link.click()


