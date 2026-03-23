from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.royalchallengers.com/rcb-squad-men')
driver.maximize_window()
sleep(3)

action=ActionChains(driver)
player=driver.find_element(By.XPATH,'(//div[@class="views-row"])[36]')
action.scroll_to_element(player).perform()
sleep(3)

for i in range(0,5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(3)
print('Done')