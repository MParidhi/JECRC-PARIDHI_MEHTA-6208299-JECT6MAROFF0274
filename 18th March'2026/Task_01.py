from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(5)
driver.find_element(By.LINK_TEXT,"Checkboxes")
driver.find_element(By.PARTIAL_LINK_TEXT,"Drop")
list_item=driver.find_elements(By.TAG_NAME,"li")
print(len(list_item))

driver.get('https://the-internet.herokuapp.com/tables')
web_site=driver.find_element(By.XPATH,'((//td[text() = "jdoe@hotmail.com"])[1]/following-sibling::td)[2]')
print(web_site.text)
del_link=driver.find_element(By.XPATH,'((//td[text()="Bach"])[1]/following-sibling::td[5]/child::a[text()="delete"])')
table2=driver.find_element(By.XPATH,'//table[2]')
hundred=driver.find_element(By.XPATH,'//table[@id="table2"]/child::tbody/child::tr[3]/child::td[4]')
print('Completed!')


driver.quit()