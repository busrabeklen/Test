import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries= driver.find_elements(By.XPATH,"//a[@class='ui-corner-all']")
print(len(countries)) #countries return as a list and give us contries list

for country in countries:
    if country.text =="India": #it will choose india on the list
        country.click()
        break #if you find india in the list dont go further then this

time.sleep(2)
#print(driver.find_element(By.ID, "autosuggest").text)
#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) #it prints on the output India
#Interview!!!! when you update value dynamicly through script how do you extract text?
#thats how you handle auto selection dropdown

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India" #IMPORTANT








