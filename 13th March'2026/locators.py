from os import name
from selenium import webdriver
from selenium.webdriver.common.by import By  ##to take id
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument('--headless')  ##healess run scripts in background without opening UI
driver=webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)

##By ID
# namee = driver.find_element(By.ID, 'name') ##find_element-->this method will return you the first occurring element if not present or any mistake(like spelling) NoSuchElementFound Exception
# phone_no = driver.find_element(By.ID, 'phone')
# # print(namee)
# print('name and phone no textfield found')

##By NAME
# nav_bar = driver.find_element(By.NAME, 'Navbar')
# print('Nav Bar found')

##By CLASS_NAME
# radio_button = driver.find_element(By.CLASS_NAME, 'form-check-input')
# print('Radio button found')

##if there are more than one radio button and we have to find the list the user find_elements
# radio_button = driver.find_elements(By.CLASS_NAME, 'form-check-input')
# print(radio_button) ##it will give a list with 9 elements
# print(len(radio_button)) ##it will give output as 9
## if there is no class name as written by us then it will give an empty list and length as 0

##By TAG_NAME
# inp=driver.find_elements(By.TAG_NAME,'input')
# print(len(inp))

#finding unique elements is disadvantage of id, class and name and advantage of css selector and also for x-path we can fine inner text

##By CSS selector-Syntax
# input[class="form-control"]
# input[type='radio']

##By CSS selector(attribute name and attribute value)
# animals = driver .find_element(By.CSS_SELECTOR, 'select[id="animals"]')
# print('worked fine')
##idhr apne select tag ke andr id ki help se find kra h

# animals=driver.find_element(By.CSS_SELECTOR, '#animals')  ## we use # for id
# print('worked fine')
# animals=driver.find_element(By.CSS_SELECTOR, '.form-control') ## we use . for class
# print('worked fine')

# <a href="http://testautomationpractice.blogspot.com/">Home</a>
##a tag will find links
# a[href="testautomationpractice"] ##*-->is for partial(first occurrence)
# a[href^="http://"] ##^-->is for starts with(first occurrence)
# a[href$=".com"] ##$-->ends with(first occurrence)

#Drawback of css selector
# You can traverse only from top to bottom
# You cant find inner text

## so we use xpath-->XML Path
## it is very efficient and performs well
## we can traverse back up-down etc
## can found any element using inner text
## disadvantages-->time consuming and complex xpath are difficult to read
## two types of xpath-->absolute xpath and relative xpath
## we will be using relative

# <html>
# <body>
# <div>
# <input id="name">
## absolute --> /html/body/div/input[@id='name']
## relative --> //input[@id='name'] -->because of 2 forward slashes it will directly forward to input

## if we have multiple input tag then, we use indexing
## (//input[@id='name'])[1]

enter_name = driver.find_elements(By.XPATH, '//input[@placeholder="Enter Name"]')
form_group = driver.find_elements(By.XPATH, '(//div[@class="form-group"])[1]')
email_length = driver.find_element(By.XPATH, '//input[@maxlength="15"]')
script_type = driver.find_element(By.XPATH, '(//script[@type="text/javascript"])[1]')
item_prop = driver.find_element(By.XPATH, '//meta[@itemprop="postId"]')
print('All worked fine')

# <a href="http://testautomationpractice.blogspot.com/">Home</a>
## if we want to find using inner tag --> (//a[text()="Home"])[1]
blog=driver.find_elements(By.XPATH, '//a[text()="Blog"]')
namee=driver.find_element(By.XPATH, '//label[text()="Name:"]')
date_picker=driver.find_element(By.XPATH, '//label[text()="Date Picker 3: (Select a Date Range)"]')
print('Worked fine')

## if text contain spaces then,
Japan=driver.find_elements(By.XPATH, '//option[contains(text(), "Japan")]')
print('Done')

