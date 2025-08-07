import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.chrome(option = chrome_options)
# chrome_options.add_argument("headless") #it will run on the headless (I will look later on)

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #this is the script we type it from console
#page will go to button (scroll down)
#whenever selenium says execute script this is java script it will execute accordingly

driver.get_screenshot_as_file("screen.png") #after run it will create file name screen.png and will take ss

