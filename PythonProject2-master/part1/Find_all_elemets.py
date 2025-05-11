import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Baseutility import BaseUtility
baseUtility = BaseUtility()

driver = baseUtility.launch_browser("chrome", "https://rahulshettyacademy.com/AutomationPractice/")
my_input_text = driver.find_elements(By.XPATH, '//input[@type="radio"]')

for i in my_input_text:
    i.click()
    print(i.get_attribute('value'))
    time.sleep(2);
