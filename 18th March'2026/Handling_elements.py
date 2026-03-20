from faulthandler import is_enabled

from selenium import webdriver
from selenium.webdriver.common.by import By ##from common we can get by, keys amd action changes
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()


male=driver.find_element(By.ID, 'male')
male.click()
print(male.is_displayed()) ##give true id this content is present on the screen
print(male.is_enabled()) ##works for button if it is enabled(only for buttons)

check=driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input')
check.click()
print(check.is_selected()) ##checks if checkboxes, radio buttons are enabled or not
monday_checkbox=driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
print(monday_checkbox.text) 

driver.quit()