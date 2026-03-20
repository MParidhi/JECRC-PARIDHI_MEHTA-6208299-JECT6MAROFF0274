from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(3)

first_name=driver.find_element(By.ID,'firstName')
first_name.clear()
first_name.send_keys('Paridhi')
sleep(2)

last_name=driver.find_element(By.ID,'lastName')
last_name.clear()
last_name.send_keys('Mehta')
sleep(2)

email=driver.find_element(By.ID,'userEmail')
email.clear()
email.send_keys('pari@gmail.com')
sleep(2)

female=driver.find_element(By.ID, 'gender-radio-2').click()
sleep(2)

mobile=driver.find_element(By.ID, 'userNumber')
mobile.clear()
mobile.send_keys('1234567890')
sleep(2)

subject = driver.find_element(By.ID, 'subjectsInput')
subject.clear()
subject.send_keys('Maths')
subject.send_keys(Keys.ENTER)
sleep(2)

subject.send_keys('English')
subject.send_keys(Keys.ENTER)
sleep(2)

hobby=driver.find_element(By.ID, 'hobbies-checkbox-3').click()
sleep(2)
hobby_text=driver.find_element(By.XPATH, '(//div[@class="form-check form-check-inline"])[6]/child::label')
print(hobby_text.text)

choose_file=driver.find_element(By.ID,'uploadPicture')
choose_file.send_keys(r'C:\Users\Dell S\Downloads\flower.jpg')
sleep(2)

address=driver.find_element(By.ID,'currentAddress')
address.clear()
address.send_keys('House No. - 141')
sleep(2)

state = driver.find_element(By.XPATH, "//div[@id ='state']")
sleep(1)
state.click()
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Rajasthan']").click()

city = driver.find_element(By.XPATH, "//div[@id = 'city']")
sleep(1)
city.click()
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Jaipur']").click()
sleep(1)

submit=driver.find_element(By.ID,'submit')
submit.click()
sleep(2)



driver.quit()