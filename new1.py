from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, ActionChains
from time import sleep
import csv
import re

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
driver = Chrome("./chromedriver.exe")

# url = "http://demowebshop.tricentis.com"
# url = "https://www.python.org/downloads/"
# url = "https://services.smartbear.com/samples/TestComplete14/smartstore"
# url = "https://demo.actitime.com/login.do"
#  url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
# url = "https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market"
# url = "file:///C:/DILEEP/Notes/Selenium/demo-html/demo.html"
# url = "https://www.monsterindia.com/"
# url = "https://www.myntra.com/boys-tshirts"
# url = 'https://vtu.ac.in/'
url = 'https://www.cleartrip.com/'
# url = 'file:///C:/DILEEP/Notes/Selenium/demo-html/loading.html'
# url = 'https://www.naukri.com/'
driver.get(url)
driver.maximize_window()

# images = driver.find_elements_by_xpath("//img")
# for image in images:
#     print(image.get_attribute('alt'))
#     sleep(2)









# handles = driver.window_handles
# sleep(5)
# for handle in handles[1::]:
#     driver.switch_to.window(handle)
#     driver.close()
# sleep(5)
#
# driver.switch_to.window(handles[0])
# sleep(1)
# driver.find_element_by_xpath('//input[@type="file"]').send_keys("C:/Users/Dileep/_selenium_new/dj.docx")


##############################################################################

# handling popup in demo page
# elements = driver.find_elements_by_xpath('//input[@class="alert"]')
#
# for element in elements:
#     element.click()
#     sleep(1)
#
# driver.find_element_by_id('delete').click()
# sleep(2)
#
# driver.switch_to.alert.accept()
# sleep(2)
#
# driver.find_element_by_id('delete').click()
# sleep(2)
#
# driver.switch_to.alert.dismiss()
# sleep(1)

##############################################################################
# program to handle java script popup
# driver.find_element_by_xpath('//input[@value="Search"]').click()
# sleep(3)
# driver.switch_to.alert.accept()
# sleep(1)

#########################################################################################
# actions = ActionChains(driver)
#
# ele1 = driver.find_element_by_xpath("//a[text()='Job search']")
# actions.move_to_element(ele1).perform()
# sleep(1)
#
# ele2 = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
# actions.move_to_element(ele2).perform()
# sleep(1)
#
# driver.find_element_by_xpath("//a[contains(text(), 'Python Jobs')]").click()
# sleep(1)
#
# driver.find_element_by_xpath("(//a[@title= 'Python Developer'] )[1]").click()
# sleep(2)
# handles = driver.window_handles
# # print(handles)
# driver.switch_to.window(handles[1])
# driver.maximize_window()
# sleep(5)
# for _ in range(6):
#     actions.send_keys(Keys.ARROW_DOWN)
# sleep(4)
# actions.send_keys(Keys.PAGE_DOWN)
# sleep(2)
# driver.find_element_by_xpath("//button[contains(text(), 'Register Now')]").click()
#
#




#################################################################################################
# ele = driver.find_element_by_xpath("//span[text()='Profile']")
# actions.move_to_element(ele).perform()
#
# driver.find_element_by_xpath("//a[text()='login / Signup']").click()

###################################################################################



# computer = driver.find_element_by_xpath("(//a[contains(text(), 'Computers')])[1]")
# actions.move_to_element(computer).perform()
# sleep(1)
#
# driver.find_element_by_xpath("(//a[contains(text(), 'Desktops')])[1]").click()
# sleep(5)
# ele = driver.find_element_by_xpath("(//a[contains(text(), 'Electronics')])[1]")
# actions.move_to_element(ele).perform()
# sleep(1)


#####################################################################################

# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         displayed = super().__call__(driver)
#         if isinstance(displayed, WebElement):
#             return displayed.is_enabled()
#         else:
#             return False
#
# wait = WebDriverWait(driver, 20)
# v = _visibility_of_element_located(('name', 'fname'))
# wait.until(v)
#
# driver.find_element_by_name('lname').send_keys('Kumar')

###################################################################


# list_box = driver.find_element_by_id('multiple_cars')
# select = Select(list_box)
#
# elements = select.options
#
# for element in elements[1::]:
#     select.select_by_visible_text(element.text)
#     sleep(2)

##############################################################################

# list_box = driver.find_element_by_id('standard_cars')
# select = Select(list_box )
# items = [item.text for item in select.options]
# print(items)
#
# for item in items[1::]:
#     if item == 'Mercedes':
#         select.select_by_visible_text(item)
#     sleep(1)

#################################################################
#  PROGRAM TO HANDLE CALENDER POP UP

driver.implicitly_wait(3)
driver.find_element_by_xpath('//div[@class="flex flex-middle p-relative homeCalender"]').click()

month = 'January 2023'
day = '26'
_xpath = f"//div[text()='{month}']/../..//div[text()='{day}']"

for _ in range(24):
    try:
        driver.find_element_by_xpath(_xpath).click()
        break
    except NoSuchElementException:
        driver.find_element_by_css_selector('svg[data-testid="rightArrow"]').click()


#######################################################################################

#  PROGRAM FOR VTU WEBSITE TO SWITCH THE WINDOW
# sleep(1)
# driver.find_element_by_link_text('English').click()
# sleep(1)
#
# driver.find_element_by_link_text('Research').click()
#
# sleep(2)
# driver.find_element_by_link_text('Research @ VTU').click()
# sleep(5)
# handles = driver.window_handles
#
# driver.switch_to.window(handles[1])
# sleep(2)
# driver.find_element_by_link_text('e - Learning Home Page').click()
# sleep(2)

#################################################################
#  PROGRAM TO HANDLE SWITCHING OF MULTIPLE WINDOWS
# driver.find_element_by_xpath("//a[text()='Twitter']").click()
# sleep(2)
# handles = driver.window_handles
# sleep(2)
# driver.switch_to.window(handles[1])
# sleep(5)
# driver.find_element_by_xpath('//input[@placeholder="Search Twitter"]').send_keys('hello world')
# sleep(1)
# driver.switch_to.window(handles[0])
# sleep(1)
# driver.find_element_by_link_text("Register").click()

##############################################################################
# PROGRAM FOR WEBDRIVERWAIT

# w = WebDriverWait(driver, 20)
# v = visibility_of_element_located(('name', 'q'))
# w.until(v)
#
# elements = driver.find_elements_by_xpath('//div[@class="footer-menu-wrapper"]/..//a')
# for element in elements:
#     print(element.text)

#########################################################################################
#  TO CHECK THE PRODUCT SELECTED LIES BETWEEN THE SELECTED RANGE
#
# driver.find_element_by_xpath('//input[@value="1476.0 TO 2818.0"]/..//div[@class="common-checkboxIndicator"]').click()
# sleep(2)
#
# prices = driver.find_elements_by_xpath('//h3[@class="product-brand"]/..//div[@class="product-price"]')
#
# for price in prices:
#     if '1476' <= re.findall('\d+', price.text)[0] <= '2818':
#         print('PASS')
#     else:
#         print('Fail')


###############################################################################33

# PROGRAM TO CHECK WHEATHER THE PAGE DISPLAY THE BRANDS WHICH SELECTED

# driver.find_element_by_xpath('//input[@value="Pepe Jeans"]/../..//label[@class="vertical-filters-label common-customCheckbox"]').click()
# sleep(1)
# brands = driver.find_elements_by_xpath('//h3[@class="product-brand"]')
# sleep(1)
# for brand in brands:
#     if brand.text == 'Pepe Jeans':
#         print('PASS')
#     else:
#         print('FAIL')
#     sleep(1)

###########################################################################3

# PROGRAM TO GET THE NAME AND DISCOUNT OF TSHIRTS WHOSE DISCOUNT ABOVE 50% IN MYNTRA WEBSITE

# discounts = driver.find_elements_by_xpath("//span[@class='product-discountPercentage']")
# discount_percentage = [discount.text for discount in discounts]
# print(discount_percentage)
#
# t_shirts = driver.find_elements_by_xpath('//span[@class="product-discountPercentage"]/../..//h4[@class="product-product"]')
# t_shirt_names = [name.text for name in t_shirts]
# print(t_shirt_names)
#
# for name, discount in zip(t_shirt_names, discount_percentage):
#     a = int(re.findall('\d+', discount)[0])
#     if a > 50:
#         print(name, a)

######################################################################
# Adding books to shopping cart and selecting one book in the cart

# books = ["Computing and Internet", 'Fiction', 'Health Book']
# for name in books:
#     print(name)
#     _xpath = f"//a[text()='{name}']/../..//input[@value='Add to cart']"
#     driver.find_element_by_xpath(_xpath).click()
#     sleep(1)

# driver.find_element_by_link_text("Shopping cart").click()
# driver.find_element_by_xpath("//a[text()='Fiction']/../..//input[@type='checkbox']").click()
sleep(3)

######################################################################################
# selecting the rating from community poll
#
# names = ['Excellent', 'Good', 'Poor', 'Very bad']
# for rating in names:
#     sleep(2)
#     _xpath = f"//label[text()='{rating}']/..//input[@type='radio']"
#     driver.find_element_by_xpath(_xpath).click()
#     sleep(1)


###############################################################################
# VALIDATE THE ACTUAL PRICES OF ALL THE BOOKS AGAINST THE EXPECTED PRICE
# expected_price = {'Computing and Internet': 10.00, 'Fiction': 24.00, 'Science': 51.00}
#
# for book, price in expected_price.items():
#     _xpath = f"//a[text()='{book}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     sleep(2)
#     if price == float(actual_price):
#         print('PASS')
#     else:
#         print('FAIL')
#     sleep(2)
#
############################################################
# To validate sunglasses

# sun_glasses = {'Sunglasses Aero': 139.00, 'Custom Sunglasses': 179.00, 'ORIGINAL COLLECTION': 149.00}
# sleep(10)
# for name, expected_price in sun_glasses.items():
#     _xpath = f"//span[text()='{name}']/../../..//span[@class='art-price']"
#     actual_price = re.findall("\d+\.\d+",driver.find_element_by_xpath(_xpath).text)[0]
#     sleep(2)
#     if expected_price == float(actual_price):
#         print('PASS')
#     else:
#         print('FAIL')
#     sleep(2)

sleep(1)
# companies = ['UPL', 'NTPC', 'IOC', 'TCS']
#
# for name in companies:
#     _xpath = f"//a[text()='{name}']/../..//td[7]"
#     price = driver.find_element_by_xpath(_xpath).text
#     print(f'{price:>10}')

##########################################################################3
# program for reading price from dyanamic values

# companies = ['AAPL', 'MSFT', 'AA', 'FB']
# for name in companies:
#     print(f'{name:>15}', end='')
# print()
# print('*' * 60)
# sleep(2)
# i = 0
# while i < 10:
#     for name in companies:
#         _xpath = f"//td[text()='{name}']/..//td[@class='price']"
#         price = driver.find_element_by_xpath(_xpath).text
#         print(f'{price:>15}', end='')
#         sleep(2)
#     print()
#     i += 1
#
#
###################################################################333
# Program to print left navigation bar text links

# elements = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
#
# for element in elements:
#     print(element.text)

########################################################################3
# Program to print bottom navigation bar text links

# elements = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
#
# for element in elements:
#     print(element.text)
#     sleep(1)


##########################################################################3
# Program to print text link in website
#
# elements = driver.find_elements_by_xpath("//div[@class='footer-main-wrapper']//a")
#
# for element in elements:
#     print(element.text)
#     sleep(1)

###########################################################################3
# program to get title of job from the webpage

# driver.find_element_by_id('SE_home_autocomplete').send_keys('Python Test Engineer')
# driver.find_element_by_xpath('//input[@value="Search"]').click()
# sleep(1)
# jobs = driver.find_elements_by_xpath('//div[@class="job-tittle"]/h3/a')
# sleep(2)
# for job in jobs:
#     print(job.text)
#     sleep(1)

########################################################################3
# Program to pass text for multiple textfiled in demo page

# names = ['hello', 'world', 'welcome', 'to', 'python', 'programming', 'is', 'fun']
#
# elements = driver.find_elements_by_xpath('//input[@name="fname"]')
# for name, element in zip(names, elements):
#     element.send_keys(name)
#     sleep(1)

#######################################################################333
#  Program to click multiple check box in demo page

# elements = driver.find_elements_by_xpath('//input[@name="download"]')
#
# for element in elements:
#     element.click()
#     sleep(1)

########################################################################3
# Program to check the actual price and expected price

# with open(r'C:\Users\Dileep\_selenium_new\smart_prices.csv') as f:
#     expected_price = {}
#     rows = csv.reader(f)
#     header = next(rows)
#     for row in rows:
#         expected_price[row[0]] = row[1]
# # print(expected_price)
# sleep(5)
# for name, price in expected_price.items():
#     sleep(2)
#     _xpath = f'//span[text()="{name}"]/../../..//span[@class="art-price" or @class="art-price art-price--offer" ]'
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     # print(actual_price)
#
#     final_price = ''.join((re.findall(r'\d*,?\d+\.\d+', actual_price))[0].split(','))
#     print(final_price)
#     if price == final_price:
#         print('PASS')
#     else:
#         print('Fail')
#

##################################################################################3
# box = driver.find_element_by_id("standard_cars")
#
# s = Select(box)
# list_ = [item.text for item in s.options]
#
# for item in list_:
#     s.select_by_visible_text(item)
#     sleep(1)

# box = driver.find_element_by_id("multiple_cars")
# s = Select(box)
# items_ = [item.text for item in s.options]
# for item in items_[1::]:
#     s.select_by_visible_text(item)
#     sleep(1)
#
# s.deselect_by_visible_text('Audi')
# print(s.first_selected_option.text)
#

