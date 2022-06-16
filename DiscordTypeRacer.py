import selenium, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Path

def login():
    global driver
    # Credential Obtainance
    link = input('Enter Discord Channel Link: ')
    mail = input('Enter Email-ID')
    pswd = input('Enter Password: ')

    if len(link)<1: link = 'https://discord.com/channels/818002930601951273/824838453308030996'
    if len(mail)<1: mail = 'dilrajgandhi@gmail.com'
    if len(pswd)<1: pswd = '3.14pi2.71e28yayeet'

    # Page Retreival
    Path.setUp(link)
    driver = Path.driver
    time.sleep(10)

    # Logging In
    driver.find_element_by_name('email').send_keys(mail)
    driver.find_element_by_name('password').send_keys(pswd)
    driver.find_elements_by_class_name('contents-18-Yxp')[1].click()
    time.sleep(5)

 

def cheat():
    inpbox = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[1]/div[2]')

    try: driver.find_elements_by_class_name('contents-18-Yxp')[8].click() #Annoying "Got It" Button Click
    except: pass

    x = int(input('Enter last msg Xpath Div Number: '))+3
    main_text_xpath = f'/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/div[1]/div/div/div/div[{x}]/div[1]/div'
    inpbox.send_keys('.typestart')
    time.sleep(8)

    main_text = driver.find_element_by_xpath(main_text_xpath).text    
    







login()