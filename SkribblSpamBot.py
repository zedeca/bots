import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PATH = r'C:\Users\pranit\Desktop\Code\chromedriver_win32\chromedriver.exe'
PATH = r'C:\Code\Python\Bots\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH) 
driver.get('https://skribbl.io/')
time.sleep(10)

inp_name = driver.find_element_by_id('inputName')
inp_name.send_keys('')
inp_name.send_keys(Keys.RETURN)
time.sleep(5)

inp_chat = driver.find_element_by_id('inputChat')
while True:
    fake_ip = str(random.randint(170,199)) + '.' + str(random.randint(100,150)) + '.' + str(random.randint(10,90)) + '.' + str(random.randint(1,200)) + '('+ str(random.randint(1, 101)) + '%)'
    inp_chat.send_keys('Hacking IP: ' + fake_ip)
    inp_chat.send_keys(Keys.RETURN)
    time.sleep(1)

    #Ⱨ₳₵₭ɆⱤ