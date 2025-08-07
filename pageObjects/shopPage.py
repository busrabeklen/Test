from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import Checkout_Confirmation


class ShopPage:

    def __init__(self, driver):
        self.driver= driver
        self.shop_link = (By.XPATH, "//a[@href='/angularpractice/shop']")
        self.product_card = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_bttn = (By.CSS_SELECTOR,"a[class*='btn-primary']")



    def add_product_to_cart(self,product_name):

        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_card)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name: #product_name coming from test
                product.find_element(By.XPATH, "div/button").click()
        # # *MEANS PARTIAL
        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()  # both same line 18 and 19


    def goToCard(self):

        self.driver.find_element(*self.checkout_bttn).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation
