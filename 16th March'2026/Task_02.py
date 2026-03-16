from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/radio-button')
sleep(3)

print(f'Title of the page is: {driver.title}')

yes=driver.find_element(By.ID, 'yesRadio')
yes.click()
yes_msg=driver.find_element(By.XPATH, '//p[@class="mt-3"]')
print(yes_msg.text)
print(yes.get_attribute('class'))
print(yes.get_attribute('id'))
sleep(5)
print(f'Title of the page is: {driver.title}')
driver.quit()