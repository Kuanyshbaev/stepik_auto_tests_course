import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form."

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("baur")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("nineelven")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("astana")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("kazakhstan")
    input5 = browser.find_element(By.CSS_SELECTOR,"button.btn")
    input5.click()

finally:
    time.sleep(10)
    browser.quit()