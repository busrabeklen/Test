import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.implicitly_wait(5)
# driver.get("https://the-internet.herokuapp.com/iframe")
# driver.switch_to.frame("mce_0_ifr") #id or name #switch to frame
# driver.find_element(By.ID, "tinymce").clear()
# driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
# driver.switch_to.default_content() #switch to normal browser ##INTERVIEW
# print(driver.find_element(By.CSS_SELECTOR,"h3").text)


#INTERVIEWW!!!! IFRAME
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,'Courses').click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("abc")
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("busra")


