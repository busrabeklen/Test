import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_exercise():
    driver= webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.XPATH,"//a[@class='blinkingText']").click()

    new_window = driver.window_handles
    driver.switch_to.window(new_window[1])
    message = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
    var = message.split("at")[1].strip().split(" ")[0] #ask this line
##"Please email us at mentor@rahulshettyacademy.com with below template to receive response"
    print(var)
    driver.close()