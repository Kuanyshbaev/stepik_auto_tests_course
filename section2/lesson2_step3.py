from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")

    num1 = browser.find_element(By.ID,"num1").text
    num2 = browser.find_element(By.ID,"num2").text
    sum1 = int(num1) + int(num2)
    sum2 = str(sum1)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum2)
    button = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
