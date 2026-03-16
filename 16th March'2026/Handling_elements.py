from selenium import webdriver
from selenium.webdriver.common.by import By ##from common we can get by, keys amd action changes
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# name=driver.find_element(By.ID,'name')## locator and 'locator expression'
# name.clear() ## clear-->will clear the previous text and enter the new one
# name.send_keys('Paridhi')
# sleep(1)
# email=driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
# email.clear()
# email.send_keys('paridhi@gmail.com') ##send_keys will send the argument written here to the particular location
# sleep(5)
#
# print(name.get_attribute('placeholder')) ##Enter Name
# print(name.get_attribute('value')) ##Paridhi

## radio buttons
# driver.find_element(By.ID, 'male').click()
# sleep(3)
#
# ## check boxes
# driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input').click()
# sleep(3)
#
# ## to find inner text
# monday_checkbox=driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
# print(monday_checkbox.text) ##or.text in above line

## toggle between male and female
# for i in range(1,5):
#     driver.find_element(By.ID,'male').click()
#     sleep(3)
#     driver.find_element(By.ID,'female').click()
#     sleep(3)

## click using if-else
# gender=input('Enter gender: ')
# if gender=='male':
#     driver.find_element(By.ID, 'male').click()
#     sleep(3)
# else:
#     driver.find_element(By.ID, 'female').click()
#     sleep(3)

## checking all check-boxes one by one printing them and unchecking backwards
days=driver.find_elements(By.XPATH, '//div[@class="form-group"][4]/child::div')
for day in days:
    day.click()
    print(day.text)
    sleep(1)

for day in days[::-1]:
    day.click()
    sleep(1)





driver.quit()

