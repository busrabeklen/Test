import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(4)
service_obj = Service()
driver = webdriver.Chrome(service= service_obj)


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    product_name = product.find_element(By.XPATH,"div/h4/a").text
    if product_name == "Blackberry" :
        product.find_element(By.XPATH,"div/button").click()
#driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()# *MEANS PARTIAL
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click() #both same line 18 and 19

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Tu")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Turkey")))
driver.find_element(By.LINK_TEXT,"Turkey").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()


message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in message
driver.close()
