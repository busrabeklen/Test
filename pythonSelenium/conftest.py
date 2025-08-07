from xml.dom.xmlbuilder import Options
import pytest
from selenium.webdriver.chrome import webdriver

from pythonSelenium.webdriver_class import initialize_browser, close_browser


def pytest_addoption(parser): #just copy-paste mendotory
    parser.addoption(
        "--browser_name", action ="store", default="chrome", help="browser selection"
    )

# @pytest.fixture(scope="function")
# def browserInstance():
#
#     driver = webdriver.Chrome()
#     driver.implicit_wait(4)
#     yield driver #driver is being send back to test_e2etestframework
#     #this code only for chrome but you can generalize
#     driver.close() #post your test function execeution


@pytest.fixture(scope='session') #start browser run all test cases and close once
def driver():
    # SetUP
    print("\n****** SetUp started ... ******")
    driver = initialize_browser()
    # driver.get("") if you have only one web site you can copy here it will use for other tests
    # driver.login_to_my_app()
    yield driver
    #TearDown
    close_browser(driver= driver , wait_time = 5)