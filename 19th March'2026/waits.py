from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://abc.com/')
driver.maximize_window()

# driver.implicitly_wait(10)
#
# ele=driver.find_element(By.XPATH,'(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(ele.get_attribute('src'))

wait_obj = WebDriverWait(driver, 10)
submit_button=wait_obj.until(EC.element_to_be_clickable((By.ID,'button'))) ##-->it will go check that element is clickable or not until 10 seconds if not found TimeOutException
submit_button.click()
##until() is a function is for waiting purpose-->until it gets satisfied

# EC.visibility_of_element_located()-->check visibility of element on UI
# EC.presence_of_element_located()-->if it is present in DOM, it will give True
# EC.invisibility_of_element_located()-->it will wait for that element to be invisible for eg pop ups, ads
# EC.alert_is_present()-->checks for alerts
# EC.presence_of_all_elements_located()-->will give list of elements present only in DOM structure not cares for UI
# EC.new_window_is_opened()-->it will wait for new tab to open
# EC.url_matches()-->to check url matches to whatever we passed to; uses regular expressions

driver.quit()
