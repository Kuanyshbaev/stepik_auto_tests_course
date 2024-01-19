from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    button = browser.find_element(By.CSS_SELECTOR,"button")
    button.click()
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)
    submit = browser.find_element(By.ID,"solve")
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
