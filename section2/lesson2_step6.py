from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)
    checkbox = browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()
    radio_button = browser.find_element(By.ID,"robotsRule")
    radio_button.click()
    button = browser.find_element(By.CSS_SELECTOR,"button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()