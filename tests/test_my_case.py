from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.login_page.login_page import Login


def test_login_page(browser):
    login_page = Login(browser)
    login_page.open()
    login_page.username()
    login_page.input_username(username)
    login_page.password()
    login_page.input_password()
    login_page.button().click()
    # a = browser.find_element()
    # a.send_keys()