from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument('--headless')
driver=webdriver.Chrome(options=opts)

driver.get('https://www.testmuai.com/selenium-playground/')
driver.maximize_window()
sleep(1)

# print('Locators using ID')
# demo_form=driver.find_element(By.ID, 'demoForm')
# print('Demo form found')
# first_name=driver.find_element(By.ID, 'inputFirstName')
# print('First name found')
# last_name=driver.find_element(By.ID, 'inputLastName')
# print('Last name found')
# email=driver.find_element(By.ID, 'inputEmail')
# print('Email found')
# mobile=driver.find_element(By.ID, 'mobileid')
# print('Mobile ID found')
# print('Locators using ID done!')

# print('Locators using CLASS')
# nav_bar=driver.find_element(By.CLASS_NAME, 'chfw-container')
# print('Nav bar found')
# selenium_container=driver.find_element(By.CLASS_NAME, 'chfw-container__selenium')
# print('Selenium container found')
# menu_link=driver.find_element(By.CLASS_NAME, 'chfw-menu-link')
# print('Menu link found')
# menu_item=driver.find_element(By.CLASS_NAME, 'chfw-menu-item')
# print('Menu item found')
# menu_description=driver.find_element(By.CLASS_NAME, 'chfw-menu-description')
# print('Menu description found')
# print('Locators using CLASS done!')

print('Locators using NAME')
first_name=driver.find_element(By.NAME, 'first_name')
print('First name found')
last_name=driver.find_element(By.NAME, 'last_name')
print('Last name found')
email=driver.find_element(By.NAME, 'email')
print('Email found')
mobile=driver.find_element(By.NAME, 'mobile_no')
print('Mobile number found')
message=driver.find_element(By.NAME, 'message')
print('Message area found')
print('Locators using NAME done!')



