from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, username):
       self.browser.find_element(username)

    def send(self, args):
        return self.browser.send_keys(*args)
