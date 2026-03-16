from selenium import webdriver
from selenium.webdriver.common.by import By ##from common we can get by, keys amd action changes
from time import sleep
from selenium.webdriver.common.keys import Keys
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)

driver.get('https://www.flipkart.com/')
driver.maximize_window()

search=driver.find_element(By.XPATH, '//form[@class="lilxh_ header-form-search"]/child::div/child::div/child::input')
search.clear()
search.send_keys('mobiles')
print(search.get_attribute('value'))
search.send_keys(Keys.ENTER)
sleep(1)

brand = driver.find_element(By.XPATH, '//div[text()="Apple"]')
brand.click()
print(brand.text)
sleep(2)
brand1 = driver.find_element(By.XPATH, '//div[text()="Google"]')
brand1.click()
print(brand1.text)
sleep(3)
image = driver.find_element(By.XPATH, '//img[@class="UCc1lI"][1]')
print(image.get_attribute('src'))
sleep(2)

driver.quit()