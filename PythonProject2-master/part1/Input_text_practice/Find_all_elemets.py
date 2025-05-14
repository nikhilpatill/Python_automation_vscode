import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Baseutility import BaseUtility

baseUtility = BaseUtility()
driver = baseUtility.launch_browser("chrome", "https://testautomationpractice.blogspot.com/")

my_input_text = driver.find_elements(By.XPATH, '//input[@type="text"and @class="input-field"]')

for i in my_input_text:
    i.click()
    i.send_keys("Apple");
    print(i.get_attribute('value'))
    time.sleep(2);