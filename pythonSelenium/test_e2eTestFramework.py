import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage
test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f) #load will convert json format to python object
    test_list =test_data["data"]  #this will be give value of data
 #this list will be store in test_list

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list) #it stores in one variable we called test_list_item
def test_e2e(driver, test_list_item): #it has to goes as an argument (test_list_item)
    # driver = webdrive.Chrome() #you dont need this lines because conftest
    #when you pass driver it picks from conftest
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    shop_page = loginPage.login(test_list_item["userEmail"] , test_list_item["userPassword"]) #after login shop page coming
    shop_page.add_product_to_cart(test_list_item["productName"]) #blackberry is spesific data#
    checkout_confirmation = shop_page.goToCard()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_adress("tur") #tur is test data
    checkout_confirmation.validate_order()

#you pass test_e2e(driver) it will only run driver fixture

##for paralel running install pluggins: pytest-xdist
#if you have 3 testcases you can run "pytest -n -3"
##pytest -n 2 -m smoke


#def test_e2e() if we dont pass driver here it cannot pick conftest driver
#lets say you have 2 fixture or more you have to spesify which one if you type driver it will execute only driver



