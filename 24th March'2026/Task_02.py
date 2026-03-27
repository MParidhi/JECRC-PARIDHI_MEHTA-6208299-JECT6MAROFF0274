from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get('https://demoqa.com/alerts')
driver.maximize_window()
sleep(2)

wait=WebDriverWait(driver,10)
driver.find_element(By.ID,'alertButton').click()
alert1=wait.until(EC.alert_is_present())
sleep(2)
alert1.accept()
sleep(2)

driver.find_element(By.ID,'timerAlertButton').click()
alert2=wait.until(EC.alert_is_present())
sleep(2)
alert2.accept()
sleep(2)

#Code to accept alert
driver.find_element(By.ID,'confirmButton').click()
alert3=wait.until(EC.alert_is_present())
sleep(2)
alert3.accept()
sleep(2)
result=driver.find_element(By.ID,'confirmResult')
assert 'Ok' in result.text,'not working'
print('Working')

#Code to dismiss alert
driver.find_element(By.ID,'confirmButton').click()
alert4=wait.until(EC.alert_is_present())
sleep(2)
alert4.dismiss()
sleep(2)
result=driver.find_element(By.ID,'confirmResult')
assert 'Cancel' in result.text,'not working'
print('Working')

driver.find_element(By.ID,'promtButton').click()
alert5=wait.until(EC.alert_is_present())
sleep(2)
msg='hello'
alert5.send_keys(f'{msg}')
sleep(2)
alert5.accept()
sleep(2)
result1=driver.find_element(By.ID,'promptResult')
assert msg in result1.text,'not working'
print('Working')
#To dismiss --> alert5.dismiss and its showing no text



