from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('https://www.amazon.in/')
sleep(3)

search=driver.find_element(By.CSS_SELECTOR, 'div[id="nav-search"]')
logo=driver.find_element(By.CSS_SELECTOR, 'a[id="nav-logo-sprites"]')
cart=driver.find_element(By.CSS_SELECTOR, 'a[id="nav-cart"]')
sign_in = driver.find_element(By.CSS_SELECTOR, 'div[id="nav-tools"] div[class="nav-div"] div[class="nav-line-1-container"] span[id="nav-link-accountList-nav-line-1"]')
all = driver.find_elements(By.CSS_SELECTOR, 'div[id="nav-xshop"] a')
print(len(all))

print('All worked fine')