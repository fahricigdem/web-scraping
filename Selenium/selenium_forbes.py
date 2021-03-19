from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome(r'C:\Users\fahri\Desktop\chromedriver.exe')

browser.get('https://www.forbes.com/the-worlds-most-valuable-brands/#5ccdf41a119c')   #browser.get('https://www.w3schools.com/python/default.asp')
WebDriverWait(browser,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="TrustArc Cookie Consent Manager"]')))
WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='call'][text()='Akzeptieren']"))).click()
time.sleep(3)

#print(browser.page_source)
#print(browser.title)

browser.get('https://www.forbes.com/companies/apple/?list=powerful-brands/#4631e6c35355')
WebDriverWait(browser,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="TrustArc Cookie Consent Manager"]')))
WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='call'][text()='Agree and Proceed']"))).click()
time.sleep(5)

browser.back()
time.sleep(2)

browser.quit()

