from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
        
hub = open('sgb-words.txt', 'r')
words = hub.read().strip()
target = '\n(...e.)\n.*'
# print(words)
x = re.findall(target, words)
res = []
for i in x:
    if 'o' in i and 'd' in i and 'r' not in i and i[1]!='o' and i[1]!='d':
        res.append(i)
print(res)