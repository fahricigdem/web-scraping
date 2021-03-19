from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


browser = webdriver.Chrome(r'C:\Users\fahri\Desktop\chromedriver.exe')

browser.get('https://www.google.com/')

#WebDriverWait(browser,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="TrustArc Cookie Consent Manager"]')))
#WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='call'][text()='Ich stimme zu']"))).click()


time.sleep(5)
#print(browser.page_source)
print(browser.title)
browser.fullscreen_window()
time.sleep(3)

browser.save_screenshot(r'C:\Users\fahri\Desktop\seleniumtest.png')
time.sleep(2)
#browser.set_window_size(600,400)
#time.sleep(5)

browser.get('https://www.google.com/search?sxsrf=ALeKk03c5H7XVv-iO_-QEHhRUfSJUATMyA%3A1599221029106&source=hp&ei=JS1SX6eoA4Xqauq_rJgI&q=kleinanzeigen&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgkIIxDqAhAnEBMyBwgjEOoCECcyBwgjEOoCECcyBwgjEOoCECcyBwgjEOoCECdQAFgAYLTXBGgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab')
#WebDriverWait(browser,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="TrustArc Cookie Consent Manager"]')))
#WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='call'][text()='Akzeptieren']"))).click()

time.sleep(3)
browser.fullscreen_window()
print(browser.title)
browser.save_screenshot(r'C:\Users\fahri\Desktop\seleniumtest1.png')

time.sleep(3)

browser.back()
time.sleep(3)

browser.quit()
