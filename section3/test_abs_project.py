from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, './/*[@placeholder = "Input your first name"]')
            input1.send_keys("baur")
            input2 = browser.find_element(By.XPATH, './/*[@placeholder = "Input your last name"]')
            input2.send_keys("nineeleven")
            input3 = browser.find_element(By.XPATH, './/*[@placeholder = "Input your email"]')
            input3.send_keys("911@mail.kz")
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            self.assertEqual(("Congratulations! You have successfully registered!"), welcome_text, "Error bratiwka")

        finally:
            time.sleep(5)
            browser.quit()

    def test_abs2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, './/*[@placeholder = "Input your first name"]')
            input1.send_keys("baur")
            input2 = browser.find_element(By.XPATH, './/*[@placeholder = "Input your last name"]')
            input2.send_keys("nineeleven")
            input3 = browser.find_element(By.XPATH, './/*[@placeholder = "Input your email"]')
            input3.send_keys("911@mail.kz")
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            self.assertEqual(("Congratulations! You have successfully registered!"), welcome_text, "Error bratiwka")

        finally:
            time.sleep(5)
            browser.quit()