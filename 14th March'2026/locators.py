from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()

# driver.get('https://www.amazon.in/')
# sleep(3)
driver.get('https://testautomationpractice.blogspot.com/')
sleep(2)

## Finding Ancestor
# all=driver.find_element(By.XPATH, '//span[text()="All"]/ancestor::div[@id="nav-main"]')
# all1=driver.find_element(By.XPATH, '//span[text()="All"]/ancestor::form[@id="nav-search-bar-form"]')
# print('done')

## Finding descendant
# //div[@id="gw-layout"]/descendant::span[@class="a-size-small a-color-base truncate-2line"]
# //div[@id="gw-layout"]/descendant::span[text()="Figurines, vases & more"]
# f_v_m=driver.find_element(By.XPATH, '//div[@id="gw-layout"]/descendant::span[text()="Figurines, vases & more"]')
# print('done')

## Finding preceding sibling, following-sibling, child, parent
# //a[text()="Fresh"]/ancestor::li/following-sibling::li[1]

##link text
# driver.find_element(By.LINK_TEXT,"Udemy Courses")
# print("FOUND")
#
# driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
# print("FOUND!")

## Practice
# sele_from_amod=driver.find_element(By.XPATH, '//td[text()="Amod"]/ancestor::tr/preceding-sibling::tr[4]/child::td[3]')
# print('Found')

# book_names=driver.find_elements(By.XPATH, '//td[text()="300"]//preceding-sibling::td[3]')
# print('Found')
# print(len(book_names))
# book_names_list=[]
# for i in book_names:
#     book_names_list.append(i.text)
# print(book_names_list)

name=driver.find_elements(By.XPATH, '//tbody[@id="rows"]//child::tr/descendant::td[1]')
name_list=[]
for i in name:
    name_list.append(i.text)
print(name_list)
print(len(name_list))


