from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver.exe")

url = "http://demowebshop.tricentis.com"
driver.get(url)
sleep(5)

driver.maximize_window()
sleep(1)

driver.minimize_window()
sleep(1)

browser_title = driver.title
print(browser_title)

new_url = driver.current_url
print(new_url)

driver.close()
