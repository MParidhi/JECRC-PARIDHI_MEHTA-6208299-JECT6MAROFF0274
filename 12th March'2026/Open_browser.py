from selenium import webdriver
# from time import sleep

##To open Chrome browser
# driver = webdriver.Chrome()
# sleep(5) ##it will close after 5 seconds

##To open Edge browser
# driver=webdriver.Edge()
# sleep(5)

##To open Firefox browser-->Firefox is not in laptop but it will still work
# driver=webdriver.Firefox()
# sleep(5)  ##Firefox will not close, it will remain open only

# driver.get("https://supertails.com") ##to open a particular URL
# driver.maximize_window() ##it will help to maximize the browser window so that all elements appear on place and easy to test
# sleep(2)

# driver.minimize_window()
# sleep(2)

# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)


# opts = webdriver.ChromeOptions()  ##a class which tells what configuration you want to provide before chrome opens
# opts.add_experimental_option('detach', True) ##now chrome will not close automatically
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://supertails.com")
# driver.maximize_window()


# opts = webdriver.EdgeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Edge(options=opts)
# driver.get("https://supertails.com")
# driver.maximize_window()




# opts = webdriver.FirefoxOptions()
# opts.set_preference('detach' ,True)
#
# driver = webdriver.Firefox(options=opts)
# driver.get("https://supertails.com")
# driver.maximize_window()


##.close--->closes the current window(other stays open) and will stay connected
##.quit--->completely close all the windows also exit the connection
# driver.close()
# driver.quit()


driver = webdriver.Chrome()
driver.get("https://supertails.com")
print(f'Title name of url is {driver.title}')
print(f'Browser name of url is {driver.name}')
print(f'Website of url is {driver.current_url}')
# Title name of url is Online Pet Store, Shop Pet Supplies and Products: Supertails
# Browser name of url is chrome
# Website of url is https://supertails.com/
