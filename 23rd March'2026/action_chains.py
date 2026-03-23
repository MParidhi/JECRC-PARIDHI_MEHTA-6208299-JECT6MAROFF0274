## is a class that contains methods for mouse and keyboard actions-->scrolling, right click, hovering, drag and drop
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver=webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(3)
#

##DRAG AND DROP
# action = ActionChains(driver)
# origin_ele=driver.find_element(By.ID, 'column-a')
# target_ele=driver.find_element(By.ID, 'column-b')
#
# action.drag_and_drop(origin_ele,target_ele).perform() ##whatever action you want to perform it will undergo that action if not ued then action chains will not work
# sleep(5)


# driver=webdriver.Chrome()
# driver.get('https://supertails.com/')
# driver.maximize_window()
# sleep(3)

##HOVERING ACTION
# action=ActionChains(driver)
# dogs=driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
# sleep(5)
# action.move_to_element(dogs).perform() ##it will hover over the element
# sleep(5)

##SCROLLING ACTION
# action=ActionChains(driver)
# cats=driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
# action.scroll_to_element(cats).perform()
# sleep(5)
#
# ##Scroll to move to the exact target eg if we give argument as 10 it will move to 10th line
# ##Scroll by will move by number given in argument eg if we are in 10th line and give 100 as argument it will move to 110
# ##in scroll by if we want to move to top then give y axis as negative and if waana go down then give y axis as positive
# action.scroll_by_amount(0,-500).perform() ##it will go up
# sleep(5)

##click-->left click
##context-click-->right click

##Keyboard actions --> have to import keys
# action = ActionChains(driver)
# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
# action.send_keys(Keys.PAGE_UP).perform() ##scrolls for 100 px by default
# sleep(5)
# action.key_down(Keys.CONTROL).send_keys('a').perform() ##key down -->press control key and a letter for select all
# sleep(5)
# action.key_up(Keys.CONTROL).perform() ##key up -->every key down should have a key up and every hold should have a release
# sleep(5)


driver=webdriver.Chrome()
driver.get(r"C:\Users\Dell S\Desktop\Pycharm\23rd March'2026\index1.html")
driver.maximize_window()
sleep(3)
action=ActionChains(driver)

driver.find_element(By.ID,'password').send_keys("pari")
sleep(3)
show_pwd=driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(3)
action.release().perform()
sleep(3)
