from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)

# action=ActionChains(driver)
# origin_ele=driver.find_element(By.ID,'draggable')
# target_ele=driver.find_element(By.ID,'droppable')
#
# action.drag_and_drop(origin_ele,target_ele).perform()
# sleep(5)
#
# assert 'Dropped!' == target_ele.text,"didn't work"
# print('done')

##For Not Greedy Drop Box
action=ActionChains(driver)
prevent=driver.find_element(By.ID,'droppableExample-tab-preventPropogation')
prevent.click()
origin_ele=driver.find_element(By.ID,'dragBox')
target_inner_ele=driver.find_element(By.ID,'notGreedyInnerDropBox')
action.drag_and_drop(origin_ele,target_inner_ele).perform()
print('Dropping in not greedy inner box 1')
print(target_inner_ele.text)
sleep(5)
#
driver.refresh()
prevent=driver.find_element(By.ID,'droppableExample-tab-preventPropogation')
prevent.click()
origin_ele=driver.find_element(By.ID,'dragBox')
target_outer_ele=driver.find_element(By.XPATH,'//p[text()="Outer droppable"]')
action.drag_and_drop(origin_ele,target_outer_ele).perform()
print('Dropping in not greedy outer box 1')
print(target_outer_ele.text)
sleep(5)

##For Greedy Drop Box
driver.refresh()
prevent=driver.find_element(By.ID,'droppableExample-tab-preventPropogation')
prevent.click()
origin_ele2=driver.find_element(By.ID,'dragBox')
target_inner_ele2=driver.find_element(By.ID,'greedyDropBoxInner')
action.drag_and_drop(origin_ele2,target_inner_ele2).perform()
print('Dropping in greedy inner box 2')
print(target_inner_ele2.text)
sleep(5)

driver.refresh()
prevent=driver.find_element(By.ID,'droppableExample-tab-preventPropogation')
prevent.click()
origin_ele2=driver.find_element(By.ID,'dragBox')
target_outer_ele2=driver.find_element(By.XPATH,'//div[@id="greedyDropBox"]/descendant::p')
action.drag_and_drop(origin_ele2,target_outer_ele2).perform()
print('Dropping in greedy outer box 2')
print(target_outer_ele2.text)
sleep(5)