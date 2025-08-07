from selenium.webdriver.common.by import By

from pageObjects.shopPage import ShopPage


class LoginPage():

    def __init__(self,driver):
        self.driver = driver #this driver will be avaliable login func
        self.username_input = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signin_bttn = (By.ID, "signInBtn")
        #if you dont add self it soesnt recognize inside login funct
        #self class instance



    def login(self, username ,password ):
        self.driver.find_element(*self.username_input).send_keys(username)
        #star will split into 2 argument such as (by id and username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signin_bttn).click()
        shop_page = ShopPage(self.driver)
        return shop_page

#po only should have action , methods , and locators