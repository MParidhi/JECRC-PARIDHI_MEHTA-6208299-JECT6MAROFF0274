from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
sleep(5)

print(f'Title of page is: {driver.title} ')
name=driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
name.clear()
name.send_keys('Admin')
sleep(3)

password=driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
password.clear()
password.send_keys('admin123')
sleep(3)

submit=driver.find_element(By.XPATH, '//button[@type="submit"]')
# submit.send_keys(Keys.ENTER)
submit.click()
sleep(3)

print(f'Current URL is: {driver.current_url}')
if 'dashboard' in driver.current_url:
    print('Successful login')
driver.quit()