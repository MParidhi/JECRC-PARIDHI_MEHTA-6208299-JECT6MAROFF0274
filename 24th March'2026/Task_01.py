from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://codepen.io/gdw96/pen/jOypoYL')
driver.maximize_window()
sleep(2)
action=ActionChains(driver)

iframe=driver.find_element(By.ID,'result')
driver.switch_to.frame(iframe)

uname=driver.find_element(By.ID,'username')
action.scroll_to_element(uname).perform()

uname.clear()
uname.send_keys('xyz')
pwd=driver.find_element(By.ID,'password')
pwd.clear()
pwd.send_keys('xxyyzz@@11223344')
show_pwd=driver.find_element(By.ID,'showPsswd')
sleep(2)
action.click_and_hold(show_pwd).perform()
sleep(2)
action.release().perform()
sleep(2)

submit=driver.find_element(By.CLASS_NAME,'submit')
submit.click()
sleep(5)
driver.back()

driver.switch_to.frame(iframe)
div=driver.find_element(By.CLASS_NAME,'container')

assert 'Registration' in div.text,'not'
print('yes')
