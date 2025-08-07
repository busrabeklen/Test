import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



####SWITCH PARENT TO CHILD WINDOW IN SELENIUM

driver= webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.XPATH,"//a[@href='/windows/new']").click()
windows_opened = driver.window_handles #property

driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(windows_opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

