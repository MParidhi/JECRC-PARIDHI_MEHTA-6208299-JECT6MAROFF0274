from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get('https://qavbox.github.io/demo/signup/')

wait=WebDriverWait(driver,10)
uname=wait.until(EC.visibility_of_element_located((By.ID,'username')))
uname.send_keys('Paridhi Mehta')

email=wait.until(EC.visibility_of_element_located((By.ID,'email')))
email.send_keys('paridhi@gmail.com')

mobile=wait.until(EC.visibility_of_element_located((By.ID,'tel')))
mobile.send_keys('0987654321')

fax_field=driver.find_element(By.ID,'fax')
if fax_field.is_enabled():
    fax = wait.until(EC.visibility_of_element_located((By.ID, 'fax')))
    fax.send_keys('302017')

file=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@name="datafile"]')))
file.send_keys(r"C:\Users\Dell S\Downloads\flower.jpg")

gender=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="sgender"]')))
select=Select(gender)
select.select_by_visible_text('Female')

exp=wait.until(EC.visibility_of_element_located((By.XPATH,'//label[@for="experience"]')))
one=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="one"]')))
one.click()

skills=wait.until(EC.visibility_of_element_located((By.XPATH,'//label[@for="skills"]')))
auto_test=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="automationtesting"]')))
auto_test.click()
html=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="html"]')))
html.click()

tools=wait.until(EC.visibility_of_element_located((By.XPATH,'//select[@id="tools"]')))
select2=Select(tools)
select2.select_by_value('cypress')

submit=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="submit"]')))
submit.click()

print('Registration Done!')
driver.quit()

