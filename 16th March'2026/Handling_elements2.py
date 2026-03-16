from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')

search=driver.find_element(By.CLASS_NAME, 'desktop-searchBar')
search.clear()
search.send_keys('dress', Keys.ENTER)
sleep(3)
# print(search.get_attribute('class')) ##whatever attribute we pass we will get that particular value
# print(search.get_attribute('value'))

# search_button=driver.find_element(By.CLASS_NAME, 'desktop-submit')
# search_button.click() ##only works for buttons
# sleep(5)
driver.quit()

##Two ways to click a button one is click and other is pass Keys.ENTER with send_keys but if we are using Keys.ENTER then we cant print value or class lie we cant use get_attribute function as it is all written in one single line so there is no time to write it in search field also if i user get_attribute after this then also it will not work