from time import sleep
from selenium.webdriver import Chrome
from pytest import fixture

# fixture are used to pass some data to test method
@fixture
def setup():
    driver = Chrome("./chromedriver.exe")
    url = "http://demowebshop.tricentis.com"
    driver.get(url)
    driver.maximize_window()
    sleep(5)
    yield driver
    driver.close()

