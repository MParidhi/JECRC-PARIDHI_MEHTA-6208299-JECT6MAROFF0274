from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# sleep(3)
# driver.get('https://www.supertails.com')
# driver.minimize_window()
# sleep(3)
# driver.maximize_window()
# sleep(3)
# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()
# sleep(3)
# driver.close()


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.supertails.com')
driver.maximize_window()
