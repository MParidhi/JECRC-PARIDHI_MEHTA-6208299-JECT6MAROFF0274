from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
driver.get(r"C:\Users\Dell S\Desktop\Pycharm\23rd March'2026\address_fields.html")
driver.maximize_window()
action=ActionChains(driver)
sleep(2)

present=driver.find_element(By.ID,'presentAddress')
permanent=driver.find_element(By.ID,'permanentAddress')

present.send_keys("JECRC, Jaipur, Rj")
sleep(2)
present.click()
action.key_down(Keys.CONTROL).send_keys("a").perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys("c").perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()
# action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() -->can use this also
permanent.click()
sleep(2)
action.key_down(Keys.CONTROL).send_keys("v").perform()
sleep(2)
action.key_up(Keys.CONTROL).perform()

