from selenium.webdriver import Chrome
from time import sleep
import csv
import re

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import  Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

driver = Chrome("./chromedriver.exe")

url = "file:///C:/DILEEP/Notes/Selenium/demo-html/loading.html"
# url = "file:///C:/DILEEP/Notes/Selenium/demo-html/progressbar.html"

driver.get(url)
driver.maximize_window()

# w = WebDriverWait(driver, 20)
# #  the element is loaded in the DOM
# # the element is visible on the page
# v = visibility_of_element_located(("name", "fname"))
# w.until(v)
#
# driver.find_element_by_name("fname").send_keys('hello')


# driver.find_element_by_xpath("//button[text()='Click Me']").click()
#
# w = WebDriverWait(driver, 20)
# v = visibility_of_element_located(('xpath', "//div[text()='100%']"))
# w.until(v)
# print('done')

# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         displayed = super().__call__(driver)
#         if isinstance(displayed, WebElement):
#             return displayed.is_enabled()
#         else:
#             return False
#
#
# w = WebDriverWait(driver, 20)
# v = _visibility_of_element_located(('name', 'fname'))
# w.until(v)
# driver.find_element_by_name("fname").send_keys('hello')

