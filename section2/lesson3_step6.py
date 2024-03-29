from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR,"button")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()