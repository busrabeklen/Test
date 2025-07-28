import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("busrabeklen0707@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("123456")



