import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5) #it will wait maximum 5 second if its find in 2 second will continue
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")  #parent-child element (there are 3 child with same name)
count = (len(results))
assert count == 3 #or count>0
for result in results:
    result.find_element(By.XPATH,"div/button").click() #it will add to cart 3 times because there is 3 items
    #just added extra part you dont have to write all xpath

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click() #we create xpath based upon text proceed
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)#because we will get text we want to print that text







