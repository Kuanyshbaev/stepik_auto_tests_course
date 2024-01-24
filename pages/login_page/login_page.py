from pages.base_page import BasePage
from selenium.webdriver.common.by import By


username_selector = (By.XPATH, ".//*[@name='tbUserName']")
password_selector = (By.XPATH, ".//*[@name='tbPassword']")
button_selector = (By.XPATH, ".//*[@id='btn-sign-in']")
input_username_selector = ['Bake_test']
input_password_selector = ('Zz123456!')
class Login(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://test.dmed.kz/")

    def username(self):
     self.find_element(By.XPATH, ".//*[@name='tbUserName']")
     self.send_keys("Bake_test")

    def password(self):
        return self.find(password_selector)

    def button(self):
        return self.find(button_selector)

    def input_username(self):
        self.send(input_username_selector)

    def input_password(self):
        return self.send(input_password_selector)