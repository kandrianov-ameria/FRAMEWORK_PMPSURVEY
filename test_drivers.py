import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# import os



url = "https://syneospmp.ameriadev.de/"


def test_chrome_url(browser):
    browser.get(url)
    assert browser.current_url == url

def test_firefox_ulr(browser):
    browser.get(url)
    assert browser.current_url == url

def test_edge_ulr(browser):
    browser.get(url)
    assert browser.current_url == url

