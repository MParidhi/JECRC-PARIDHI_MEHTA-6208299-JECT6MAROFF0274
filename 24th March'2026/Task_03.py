from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()
sleep(2)

main_window=driver.current_window_handle

new_tab=driver.find_element(By.ID,'tabButton').click()
all_windows=driver.window_handles
print(len(all_windows))
driver.switch_to.window(all_windows[-1])
sleep(2)
content1=driver.find_element(By.ID,'sampleHeading')
assert 'This is a sample page' in content1.text,'New tab does not work properly'
print('New Tab worked properly')
driver.close()
driver.switch_to.window(main_window)
sleep(2)

new_window=driver.find_element(By.ID,'windowButton').click()
all_windows=driver.window_handles
print(len(all_windows))
driver.switch_to.window(all_windows[-1])
sleep(2)
content2=driver.find_element(By.ID,'sampleHeading')
assert 'This is a sample page' in content2.text,'New window does not work properly'
print('New window worked properly')
driver.close()
driver.switch_to.window(main_window)
sleep(2)

msg_new_window=driver.find_element(By.ID,'messageWindowButton').click()
all_windows=driver.window_handles
print(len(all_windows))
driver.switch_to.window(all_windows[-1])
sleep(2)
driver.close()
driver.switch_to.window(main_window)
sleep(2)
