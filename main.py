#
from selenium import webdriver

the_browser_to_go = 'chrome'

driver = None

if the_browser_to_go == 'chrome':
    driver = webdriver.chrome('browser-drivers/ch')