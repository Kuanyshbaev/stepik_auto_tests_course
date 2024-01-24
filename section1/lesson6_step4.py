import time

#from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
# selenium.webdriver.support import wait

link = "https://test.dmed.kz/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    username = browser.find_element(By.XPATH, ".//*[@name='tbUserName']")
    input_username = username.send_keys("Bake_test")
    password = browser.find_element(By.XPATH, ".//*[@name='tbPassword']")
    input_password = password.send_keys("Zz123456!")
    button = browser.find_element(By.XPATH, ".//*[@id='btn-sign-in']").click()

    #browser.switch_to.window(second_window)
    time.sleep(1)
    # self.wait.until(EC.visibility_of_all_elements_located)
    webdriverwait = browser.find_element(By.XPATH, "//*[@class='open-overlay' and text()='Модули']").click()
    profylaxis = browser.find_element(By.XPATH, ".//*[@href='https://prof-test.dmed.kz/']").click()
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

finally:
    time.sleep(10)
    browser.quit()