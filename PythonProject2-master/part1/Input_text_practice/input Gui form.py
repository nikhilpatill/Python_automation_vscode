import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Baseutility import BaseUtility
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


baseUtility = BaseUtility()
driver = baseUtility.launch_browser("chrome", "https://testautomationpractice.blogspot.com/")

#name = driver.find_elements(By.XPATH, '//input[@id="name"]')
webdriverwait = WebDriverWait(driver, 10)
name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="name"]')))

if name.is_displayed():
    name.click()
    name.send_keys("Apple")
    print("input value add successfully ",name.get_attribute('value'))


Email= webdriverwait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="email"]')))
if Email.is_displayed():
    Email.click()
    Email.send_keys("nik234@gmail.com")
    print("input value add successfully ",Email.get_attribute('value'))

phone = webdriverwait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="phone"]')))
if phone.is_displayed():
    phone.click()
    phone.send_keys("12030040040")
    print("input value add successfully ",phone.get_attribute('value'))
    
   
time.sleep(2)
Address = driver.find_element(By.XPATH, '//textarea[@id="textarea"]') 
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Address)
#Address = webdriverwait.until(EC.presence_of_element_located((By.XPAth, '//textarea[@id="textarea"]')))
if Address.is_displayed():
    Address.click()
    Address.send_keys("pune maharashtra")
    print("input value add successfully ",Address.get_attribute('value'))
    
Gender = webdriverwait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="male"]')))
if Gender.is_displayed() or Gender.isvisible():
    Gender.click()
    print("input value add successfully ",Gender.get_attribute('value'))
   
   
days= driver.find_elements(By.XPATH,'//input[@class="form-check-input" and @type="checkbox"]') 
#days=webdriverwait.until(EC.presence_of_element_located((By.XPATH,'//select[@type="checkbox"]')))
for i in days:
    if i.is_enabled():
     i.click()
    print("input value add successfully ",i.get_attribute('value'))