#have to import module called os, nd it will be stored wherever we are working
import os ##have all the methods to set the path, create folders etc..(Here we are using to make a screenshot folder)
from operator import contains

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

folder=os.path.join(os.getcwd(), 'screenshots') ##->it will get the path whatever we are giving and join two things the directory and folder name
##will get the current working dir and join screenshots folder to it
os.makedirs(folder, exist_ok=True) ##exist_ok-->will check if folder is present or not, if there will move on if not will create one


driver=webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
action=ActionChains(driver)
sleep(2)

##used when there is code error so it will take screenshot of the last page...
##two methods-->screenshot of whole page and second to take of a particular element
##whole page-->save_screenshot with two argument one is folder name and second is screenshot file name.png(png always) separated by /
##particular element-->use .screenshot
driver.save_screenshot(f'{folder}/full_page.png') ##now these screenshot will be stored in that particular folder


ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
action.scroll_to_element(ele).perform()
sleep(1)

ele.screenshot(f'{folder}/cheery_red.png')
sleep(2)

##important
# //img[contains(@alt,"cherry-patterned")]
##this is another way to use contains with attribute name and attribute value
##contains(text(),"")-->only works for inner text













