# load selenium module - to call selenium module related functions
from selenium import webdriver

# load time module - to call time module related functions
import time

# load os module - to call the os module related functions
import os

# from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys

the_browser_to_go = 'firefox'

driver = None

project_folder_path = os.path.dirname(__file__)

# The browser driver selection
if the_browser_to_go == 'chrome':
    driver = webdriver.Chrome(os.path.join(project_folder_path, 'browser-drivers\\chromedriver_win32\\chromedriver.exe'))
elif the_browser_to_go == 'edge':
    driver = webdriver.Edge(os.path.join(project_folder_path, 'browser-drivers\\edgedriver_win64\\msedgedriver.exe'))
elif the_browser_to_go == 'firefox':
    driver = webdriver.Firefox(executable_path=os.path.join(project_folder_path, 'browser-drivers\\geckodriver-v0.30.0-win64\\geckodriver.exe'))
# load-site
site_url = 'https://duckduckgo.com/'
driver.get(site_url)
time.sleep(2)

# interact-elements-input
search_field = 'search_form_input_homepage'
driver.find_element_by_id(search_field).send_keys("random number")
time.sleep(2)

# interact-elements-search
search_icon = 'search_button_homepage'
driver.find_element_by_id(search_icon).send_keys(Keys.ENTER)


time.sleep(5)
driver.close()
