from selenium.webdriver import Chrome
# from time import sleep
# import csv
# driver = Chrome("./chromedriver.exe")
#
# url = "http://demowebshop.tricentis.com/books"
# driver.get(url)

# def read_csv(path):
#     with open(path) as f:
#         reference = {}
#         rows = csv.reader(f)
#         header = next(rows)
#         for row in rows:
#             reference[row[0]] = float(row[1])
#     return reference
#
# res = read_csv('gogou')
#
# for gadget, price in res.items():
#     _xpath = f'//a[text()="{gadget}"]/../..//span[@class="price actual-price"]'
#     actual_price = driver.find_element_by_xpath(_xpath)
#     if float(actual_price) == price:
#         print('PASS')
#     else:
#         print('FAIL')

a = ['13245', '43577']
l = []
for i in a:
    l.append(int(i))
print(l)

