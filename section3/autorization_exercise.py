import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser):
    link = f"https://stepik.org/lesson/236895/step/1/"
    browser.get(link)
    login = browser.find_element(By.ID, "ember33")
    login.click()
    input_login = browser.find_element(By.ID, "id_login_email")
    input_login.send_keys("baur.jaguar@gmail.com")
    input_password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    input_password.send_keys("Sk!465852Sk!")
    enter = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader")
    enter.click()
    time.sleep(5)