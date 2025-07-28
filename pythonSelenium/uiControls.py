import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PythonBasics.dictionary import value

driver= webdriver.Chrome()

#handling checkbox dynamically

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']") #this is not unique xpath

print(len(checkboxes))

for checkbox in checkboxes: #I want to click option2(checkboxes is list)
    if checkbox.get_attribute("value") == "option2": #value=option2 (you can see on the website)
        checkbox.click()
        assert checkbox.is_selected()
        break

radio_button = driver.find_elements(By.XPATH, "//input[@name='radioButton']") #this xpath not uniqe that's why we pass index
radio_button[2].click()
assert radio_button[2].is_selected()

time.sleep(2)

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

#ALERTS













