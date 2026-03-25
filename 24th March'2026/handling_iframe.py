##iframe is an inner frame
##Nested HTML will start with <iframe> and then <html> tag
##any field eg text field inside an iframe will not work unless we switch to that iframe as control is with outer HTML
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(2)

# iframe=driver.find_element(By.ID,'singleframe') ##finding iframe
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123') ##finding text-box inside iframe
# sleep(5)


driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
sleep(2)
nested_iframe=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)
sleep(2)
inner_iframe=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123')
sleep(2)

driver.switch_to.parent_frame() #switch to parent frame (move one step back)
driver.switch_to.default_content() #switch to default page (move to most outer html)











