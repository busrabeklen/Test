import time

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber -1 Kg' , 'Raspberry - 1/4 Kg' , 'Strawberry - 1/4 Kg']

driver = webdriver.Chrome()
 #that applies every steps
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
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

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@type='text']")))
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("rahulshettyacademy")
#we use explicit wait because code apply takes more than 2 second


driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
#expected condition apply only one step
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)#because we will get text we want to print that text



#Sum validation
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")


sum = 0
for price in prices:
    sum = sum + int(price.text) #48+160+180 (we have to convert string to int) because sum is int

print(sum)

total_amount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert sum == total_amount


####total after discount price < total amount
discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text) #it comes string we have to convert float because discoun like 234.5
assert total_amount > discount