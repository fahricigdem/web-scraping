from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome(r'C:\Users\fahri\Desktop\chromedriver.exe')

browser.get('https://www.forbes.com/the-worlds-most-valuable-brands/#5ccdf41a119c')   #browser.get('https://www.w3schools.com/python/default.asp')
time.sleep(5)

browser.fullscreen_window()
time.sleep(2)

browser.save_screenshot(r'C:\Users\fahri\Desktop\seleniumtest.png')
time.sleep(2)

browser.quit()

