from selenium import webdriver
def setUp(website):
    global driver
    path_chromedriver =  r"C:\Users\pranit\Code\Python\Bots\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(path_chromedriver, options=options)
    driver.get(website)