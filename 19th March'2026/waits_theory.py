## two types of waits-->unconditional and conditional
## unconditional wait--> sleep which stops the python execution which is a bad practice
## conditional wait is of two types-->implicit and explicit
## IMPLICIT WAIT
    ##driver.implicitly_wait(5)
    ##condition-->it should be found in the DOM structure
    ##It will not wait for full 5 seconds it will start interacting just after element if found(in DOM structure)
    ##If the element is not found in 5 seconds then 6th second it will throw exception-->NoSuchElementFound
    ##applicable only for driver.find_element
    ##if element in DOM structure and not visible in UI still it will work-->Disadvantage
    ##it only cares about finding element in DOM structure

## EXPLICIT WAIT
    ##can give multiple conditions
    ##have to import--> from selenium.webdriver.support.wait import WebDriverWait
    ##also import--> from selenium.webdriver.support import expected_conditions as EC-->this will have all the conditions
    ##it will wait for a particular element until the condition is satisfied
    ##confined to particular element it is not global like implicit wait as diff element have diff conditions to satisfy
    ##it will wait for both DOM and UI to load before giving output
    ## We use this to avoid the time difference of UI and DOM structure
    ## Example
    ## 0->>DOM
    ## 1->>UI
    ## 2->>Button visible
    ## 3->>Condition check
    ## Then further..
    ## If not found till timeout time then TimeOutException
    ## By default polling frequency of-->500 milliseconds-->0.5sec

##One more time of wait
##Altering polling frequency in explicit wait is called Fluent wait
##Just have to pass wait_obj = WebDriverWait(driver, 10,poll_frequency=200)

##How to handle synchronization error
## First is explicit wait
## Another is writing better XPATH's