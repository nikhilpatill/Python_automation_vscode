import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Baseutility import BaseUtility
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC



baseUtility = BaseUtility()
driver = baseUtility.launch_browser("chrome", "https://testautomationpractice.blogspot.com/")
try:
    input_text_1 = driver.find_element(By.XPATH, "//input[@name='dummy']")
    print("Input text field exists.")
except NoSuchElementException:
    print("Input text field does not exist.")
 

