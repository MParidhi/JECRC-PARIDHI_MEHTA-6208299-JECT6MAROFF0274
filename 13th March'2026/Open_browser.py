from selenium import webdriver
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument('--headless')  ##healess run scripts in background without opening UI
driver=webdriver.Chrome(options=opts)

driver.get('https://www.myntra.com')
sleep(4)
print('Its working fine')