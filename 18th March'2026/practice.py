from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(5)


home=driver.find_element(By.XPATH, '//a[@data-group="home"]')
print(home.text)

# assert 'HOME' in home.text,'didnt find HOME'
# print('success')

assert 'HOME'==home.text,'didnt find'
print('success')

driver.quit()