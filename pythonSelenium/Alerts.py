import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

name ="busra"
driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)
driver.find_element(By.ID,"alertbtn") .click()
alert = driver.switch_to.alert
assert alert.text == "Hello busra, share this practice page and share your knowledge"
alert.accept() #okay
#alert.dismiss() #cancel

time.sleep(2)



