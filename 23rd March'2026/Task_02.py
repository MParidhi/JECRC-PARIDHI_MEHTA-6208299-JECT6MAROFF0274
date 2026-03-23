from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(1)

actions = ActionChains(driver)
women=driver.find_element(By.XPATH,'(//a[text()="Women"])[1]')
sleep(3)
actions.move_to_element(women).perform()
sleep(3)

dress=driver.find_element(By.XPATH,'(//div[@class="desktop-paneContent"])[2]/descendant::li/descendant::a[text()="Dresses"]')
dress.click()
sleep(3)

row=driver.find_element(By.XPATH,'//ul[@class="results-base"]/child::li[17]')
actions.scroll_to_element(row).perform()
sleep(3)

