from selenium import webdriver
from time import sleep
browser=[webdriver.Chrome(),webdriver.Firefox(),webdriver.Edge()]
for i in browser:
    i.maximize_window()
    sleep(2)
    i.close()
