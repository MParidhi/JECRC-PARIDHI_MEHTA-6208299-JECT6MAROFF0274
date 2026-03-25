##sometimes ui is not scrolling so we use javascript executor-->works on backend like forcefully telling to scroll or any other action
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(3)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') ##-->scroll to the bottom-most of the page
sleep(5)

##to top of the page(origin)
driver.execute_script('window.scrollTo(0,0);') ##scroll to exact point
sleep(5)

driver.execute_script('window.scrollBy(0,500);') ##500px down from origin
sleep(5)
driver.execute_script('window.scrollBy(0,-200);') ##from 500px to 200px up-->scrolls by reference
sleep(5)


##scroll to-->only positive value, if negative value it will consider as 0-->but its sometimes working sometimes not
##scroll by-->want to go up->negative value

#scrolling to element
ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
driver.execute_script('arguments[0].scrollIntoView();',ele)
sleep(5)

#clicking
click_ele=driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')
driver.execute_script('arguments[0].click();',click_ele)
sleep(5)













