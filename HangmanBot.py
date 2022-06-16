from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import Path

Path.setUp('https://www.hangmanwords.com/play')
# Path.setUp('https://www.hangmanwords.com/play/hard-words')
driver = Path.driver
driver.implicitly_wait(2)
# play = driver.find_element_by_link_text('Play')
# play.click()
driver.implicitly_wait(5)

def main():
    word = driver.find_element_by_id('word')
    print(word.text)
    for letter in word.text:
        pyautogui.press(letter)

    try:
        next_match_btn = driver.find_element_by_class_name('new-word')
        next_match_btn.click()
    except: pass

while True:
    main()