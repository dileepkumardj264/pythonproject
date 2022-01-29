from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver.exe")

url = "http://demowebshop.tricentis.com"
driver.get(url)

driver.find_element_by_xpath('//a[@class = "ico-register"]').click()
driver.find_element_by_xpath('(//input[@name="Gender"])[1]').click()
driver.find_element_by_xpath('//input[@id="FirstName"]').send_keys('Dileep')
driver.find_element_by_xpath('//input[@id="LastName"]').send_keys('Kumar')
driver.find_element_by_xpath('//input[@id="Email"]').send_keys('dileepkumar.dj@gmail.com')
driver.find_element_by_xpath('//input[@name="Password"]').send_keys('Darwin264')
driver.find_element_by_xpath('(//input[@type="password"])[2]').send_keys('Darwin264')
driver.find_element_by_xpath('//input[@value="Register"]').click()
