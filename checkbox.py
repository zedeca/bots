from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

WEBSITE = "https://checkboxrace.com/"
PATH = r"C:\Users\pranit\Code\Python\Bots\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options=options)
driver.get(WEBSITE)

checkboxes = driver.find_elements_by_css_selector('body > div.checkboxes > input[type=checkbox]')
for checkbox in checkboxes:
    try:
        checkbox.click()
    except: 
        time.sleep(5)
        checkbox.click()
    else:
        time.sleep(0.02)
