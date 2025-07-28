import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url) #print just see in the output










time.sleep(2)


