import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
browserSortedVeggies =[]

#click on column header
#collect all veggie names-> veggieList (b,a ,c)
#sort this veggie list -> newSortedList (a, b ,c)
#veggielist == newsortedlist

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click() #step 1
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]") #it il give list like almond, banana , strawbery
for element in veggieWebElements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy()

browserSortedVeggies.sort() #step 2
assert browserSortedVeggies == originalBrowserSortedList #step3
 #section 15/60 watch one more time

