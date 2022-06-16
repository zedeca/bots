import Path
import time
from selenium import webdriver


def main():
    game = input("Games:\n1. Swirl\n2. Switch\n3. Break\nEnter Option: ").strip()
    mins = input("Minutes (1, 3, 5): ").strip()
    config()
    if game == '1':
        swirl()
    if game == '2':
        switch(mins)
    if game == '3':
        _break()

def config():
    global driver
    website = "https://thezen.zone/"
    Path.setUp(website)
    driver = Path.driver
    
    games = driver.find_element_by_css_selector("#root > div > div > header > div > a")
    games.click()

    driver.implicitly_wait(5)

def swirl():
    pass

def switch(mins):
    switch_btn = driver.find_element_by_css_selector("#root > div > div > section > div > a:nth-child(2)")
    switch_btn.click()
    
    driver.implicitly_wait(5)

    mins_btn = driver.find_element_by_link_text(mins)
    mins_btn.click()

    driver.implicitly_wait(5)
    switches = driver.find_elements_by_class_name("slider")
    for switch in switches:
            try:
                switch.click()
            except:
                time.sleep(0.2)
                switch.click()

def _break():
    pass

main()