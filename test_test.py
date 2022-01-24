
# # from seleniumwire import webdriver 
# from selenium.webdriver.common.by import By


# import time
# import json
# # import requests as rq


# # url = "https://syneospmp.ameriadev.de/"

# # request_url = "https://api-syneospmp.ameriadev.de/country"

# # country_ispresent = None

# # def test_go_to(browser):
# #     browser.get(url)

# #     time.sleep(10)

    
# #     for request in browser.requests:
# #         if request.response and request.url.startswith(request_url):
# #             country_ispresent = request
    
# #     print(f"\nPrinting {request.url}")
# #     print(f"\nPrinting {request.response.headers}")
# #     print(f"\nPrinting {request.response.status_code}")

# #     payload = rq.get(request_url)
# #     js = json.loads(payload.text)
# #     code = payload.status_code
# #     print(js, code)

# # pytest -s --browser_name=chrome test_test.py



# def test_go_to_home_page(browser):
#     page = HomePage(browser, HPS.homepage_url)
#     page.go()
#     page.maximize()

assert_success("one")
print(assert_success().__dir__)


