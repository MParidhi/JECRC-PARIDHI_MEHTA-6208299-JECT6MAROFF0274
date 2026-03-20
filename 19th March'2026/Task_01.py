#1.got to abc site
#2. fetch all image links of svg banners (use for loop), use explicit waits instead of find element, use presence of element located
#3.pause the loading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://abc.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)
images=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="hero-items"]/descendant::picture/child::img')))
for image in images:
    print(image.get_attribute('src'))
##presence_of_all_elements_located-->this is used as all elements are not in UI at once but they are in DOM structure and also there are many elements therefore we have used all_elements

print('All links shown')

driver.quit()