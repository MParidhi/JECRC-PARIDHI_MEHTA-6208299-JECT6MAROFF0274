from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/login')
sleep(3)

username=driver.find_element(By.XPATH, '//input[@name="username"]')
password=driver.find_element(By.XPATH, '//input[@id="password"]')
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
elemental_selenium=driver.find_element(By.XPATH, '//a[text()="Elemental Selenium"]')
login_page=driver.find_element(By.XPATH, '//h2[contains(text(), "Login Page")]')
print('All worked fine!')
