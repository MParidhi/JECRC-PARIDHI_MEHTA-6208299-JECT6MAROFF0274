from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(2)
# parent_window=driver.current_window_handle ##will return the particular window handle
# print(parent_window)
#
# driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
# sleep(2)
# all_windows=driver.window_handles ##return a list of all the windows that are present
# #will switch using indexing, index 0 will always be parent window and recent most in -1
# print(len(all_windows))
# driver.switch_to.window(all_windows[-1])
# print(driver.current_window_handle)
# assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
# print('done')
# ##if we use driver.close() here it will only close the window but will not switch the control back to parent window

# driver.switch_to.window(parent_window) #3switch back to parent window
# sleep(2)

#opening a website in new window
# driver.switch_to.new_window('window')
# driver.get('https://www.cricbuzz.com/') ##open in the current tab

driver.switch_to.new_window('tab')
driver.get('https://www.cricbuzz.com/') ##open in new tab


















