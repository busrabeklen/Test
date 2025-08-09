import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME , 'email').send_keys('hello@gmail.com')
driver.find_element(By.ID , "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID , "exampleCheck1").click()

#create XPATH -- //tagname[@attribute ='value'] -- //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME , 'alert-success').text
print(message)
driver.find_element(By.XPATH,"//input[@value='option1']").click()

#Static DropDown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female") #same




#create CSS -- tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Busra")

assert "Success" in message



#always we cant find name or id or maybe not unique thats why use xpath mostly
time.sleep(2)

