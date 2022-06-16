import time
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pg

def gameSetUp():
    global driver, PATH
    PATH = r'C:\Code\Python\Bots\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get('http://www.higherlowergame.com/')
    time.sleep(2)
    classic_mode = driver.find_element_by_xpath('/html/body/div/div/span/section/div[2]/div/button[1]')
    classic_mode.click()
    time.sleep(2)

def getWords():
    global words
    words = driver.find_elements_by_class_name('term-keyword__keyword')[:2]
    return words

def statsSetUp(words):
    statdriver = webdriver.Chrome(PATH)
    word1 = words[0].text.replace(' ', '%20')
    word2 = words[1].text.replace(' ', '%20')
    # statdriver.get(f'https://trends.google.com/trends/explore?q={word1},{word2}')
    statdriver.get(f'https://trends.google.com/trends/explore?date=today%203-m&q={word1},{word2}')
    pg.click()
    pg.press('enter')

    try:
        error_tag = statdriver.find_element_by_class_name('widget-error-title')
        word1 = word1[1:-1]
        word2 = word2[1:-1]
        statdriver.get(f'https://trends.google.com/trends/explore?date=today%203-m&q={word1},{word2}')
    except: pass
    a = statdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/ng-include/div/ng-include/div/bar-chart/div/div/div[1]/div/svg/g[1]/g[1]/g[2]/g/rect[2]')

gameSetUp()
for i in range(5):
    getWords()
    statsSetUp(words)
