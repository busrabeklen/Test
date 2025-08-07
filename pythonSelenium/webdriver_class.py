import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Webdriver class
def initialize_browser():
    options = Options()  # configuration of your driver
    options.add_argument("--guest")
    options.add_experimental_option("detach", True)  # hold the page
    options.page_load_strategy = 'normal'  # instruction to wait for you find_element()
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)  # retry to find for maxim 10 sec
    return driver



def close_browser(driver, wait_time):
    # driver.minimize_window()
    time.sleep(wait_time)
    driver.quit()
    print(f"Successfully completed the {__file__}")