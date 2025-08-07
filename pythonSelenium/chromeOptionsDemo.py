import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximize")
options.add_argument("--headless") #it will run backend
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options= options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title) #there is no browser because we said headless