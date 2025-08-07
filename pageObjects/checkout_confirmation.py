from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_bttn = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "Turkey")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_bttn = (By.XPATH, "//input[@type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")




    def checkout(self):
        self.driver.find_element(*self.checkout_bttn).click()





    def enter_delivery_adress(self,countryName):

        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option)) #we dont need star
        self.driver.find_element(*self.country_option).click()

        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_bttn).click()



    def validate_order(self):
        message = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in message