from selenium import webdriver
import time

WEBSITE = "https://checkboxolympics.com/"
PATH = r"C:\Users\pranit\Code\Python\Bots\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options=options)
driver.get(WEBSITE)

ready = driver.find_element_by_class_name("readyButton")
ready.click()
time.sleep(3)
checkboxes = driver.find_elements_by_css_selector("#root > div > div.sportsWrapper > div.theSport > div:nth-child(2) > input[type=checkbox]")
for checkbox in checkboxes:
    checkbox.click()