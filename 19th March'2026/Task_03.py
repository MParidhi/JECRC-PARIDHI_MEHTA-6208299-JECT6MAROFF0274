from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')

wait=WebDriverWait(driver,10)
search=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="twotabsearchtextbox"]')))
search.send_keys('dress')
option4=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@id="sac-suggestion-row-4"]')))
option4.click()
sort=wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-button-text a-declarative"]')))
sort.click()
new=wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@id="s-result-sort-select_4"]')))
new.click()
free_shipping=wait.until(EC.visibility_of_element_located((By.XPATH,'//span[@class="a-size-base a-color-base"]')))
free_shipping_btn=wait.until(EC.element_to_be_clickable((By.XPATH,'(//i[@class="a-icon a-icon-checkbox"])[3]')))
free_shipping_btn.click()
price=wait.until(EC.visibility_of_element_located((By.XPATH,'//span[@class="a-price-whole"]')))
name=wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"])[1]')))
print(name.text, "=", price.text )

driver.quit()