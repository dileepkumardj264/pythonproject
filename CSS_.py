from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver.exe")

url = "http://demowebshop.tricentis.com"
driver.get(url)

driver.find_element_by_css_selector('a[class="ico-register"]').click()
driver.find_element_by_css_selector('input[id="gender-male"]').click()
driver.find_element_by_css_selector('input[id="FirstName"]').send_keys('Dileep')
driver.find_element_by_css_selector('input[id="LastName"]').send_keys('Kumar')
driver.find_element_by_css_selector('input[name="Email"]').send_keys('dileepkumar.dj@gmail.com')
driver.find_element_by_css_selector('input[name="Password"]').send_keys('Darwin264')
driver.find_element_by_css_selector('input[name="ConfirmPassword"]').send_keys('Darwin264')
driver.find_element_by_css_selector('input[id="register-button"]').click()
