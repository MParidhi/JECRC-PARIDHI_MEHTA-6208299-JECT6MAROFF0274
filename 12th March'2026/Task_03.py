from selenium import webdriver
from time import sleep
browser=[webdriver.Chrome(),webdriver.Edge(),webdriver.Firefox()]

for i in browser:
    i.get('https://www.google.com')
    print(f'Title name of url is {i.title}')
    print(f'Browser name of url is {i.name}')
    print(f'Website of url is {i.current_url}')
    i.quit()

