from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
# driver.get('https://www.lenskart.com')
# driver.maximize_window()
# sleep(5)

# eye=driver.find_element(By.ID,'lrd1')
# print(eye.text)

##assert-->a keyword that checks if statement true or false; If true it will go further with code execution but if false it will throw assertion error
# assert 'EYEGLASSES' in eye.text,'didnt find' ##condition, false block statement
# print('found')
## if condition is true then it will print found nd quit the driver but if false it will give assertion error as didnt find and will not quit
## assert is used for validation

driver.get('https://www.lenskart.com/lenskart-studio-lk-e18185-gunmetal-eyeglasses.html')
sleep(5)
check=driver.find_element(By.XPATH,'//h4[text()="Check"]')
sleep(2)
check.click()
print(check.is_enabled())
sleep(5)

check2=driver.find_element(By.XPATH,'//div[@class="sc-a3b31f26-14 fDEfLM"]')
print(check2.is_enabled())


driver.quit()

