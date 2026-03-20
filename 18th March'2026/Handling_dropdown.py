## to handle dropdowns present in "select" tag we have to import a class called select and user methods under that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

# driver=webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()

# country_dropdown=driver.find_element(By.ID, 'country')
# dropdown=Select(country_dropdown)
#
# dropdown.select_by_value('australia')
# sleep(5)
# dropdown.select_by_index(3)
# sleep(5)
# dropdown.select_by_visible_text('Japan')
# sleep(5)
##In XPATH indexing start from 1 but here it will start from 0


driver=webdriver.Chrome()
driver.get('https://www.lenskart.com/')
driver.maximize_window()

search=driver.find_element(By.XPATH, '//input[@placeholder="What are you looking for?"]')
search.send_keys('sunglasses', Keys.ENTER)
sleep(3)

sort_dropdown=driver.find_element(By.ID,'sortByDropdown')
sort=Select(sort_dropdown)

# sort.select_by_value('saving')
sort.select_by_value('low_price')
sleep(5)

img=driver.find_element(By.XPATH,' (//div[@class="sc-bf32d8a7-0 gOVKHN"]/descendant::p[@class="sc-23b7d3eb-2 dQrJBg"])[1]')
print(img.text)

driver.quit()