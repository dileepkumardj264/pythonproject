from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver.exe")

url = "http://demowebshop.tricentis.com/books"
driver.get(url)

# a = driver.find_elements_by_tag_name("a")
# print(a)
# b = driver.find_elements_by_class_name("top-menu-triangle")
# print(b)

# driver.find_element_by_xpath("//a[text()='Log in']").click()
driver.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@type='button']").click()


