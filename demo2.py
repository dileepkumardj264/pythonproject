
from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver.exe")

url = "http://demowebshop.tricentis.com"
driver.get(url)

driver.find_element_by_link_text("Register").click()
driver.find_element_by_id("gender-male").click()
driver.find_element_by_id("FirstName").send_keys("Dileep")
driver.find_element_by_name("LastName").send_keys("Kumar")
driver.find_element_by_id("Email").send_keys("dileepkumar.dj@gmail.com")
driver.find_element_by_id("Password").send_keys("Darwin264")
driver.find_element_by_name("ConfirmPassword").send_keys("Darwin264")
driver.find_element_by_id("register-button").click()
driver.find_element_by_link_text("Log in").click()
driver.find_element_by_id("Email").send_keys("dileepkumar.dj@gmail.com")
driver.find_element_by_id("Password").send_keys("Darwin264")
driver.find_element_by_class_name("button-1.login-button").click()

