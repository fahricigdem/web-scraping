from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'C:\Users\fahri\Desktop\chromedriver.exe')
browser.get('https://www.linkedin.com/')
#browser.fullscreen_window()
time.sleep(3)

login = browser.find_element_by_xpath('/html/body/nav/a[3]')
login.click()
time.sleep(3)

email = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')
email.send_keys('fahricigdem34@gmail.com')
password.send_keys('##########')

login_buton = browser.find_element_by_css_selector('#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button')
login_buton.click()
time.sleep(5)

search_field = browser.find_element_by_xpath('//*[@id="ember16"]/input')
search_field.send_keys('#python')
search_field.send_keys(Keys.RETURN)
time.sleep(5)

contacts = browser.find_element_by_xpath('//*[@id="ember23"]/span')
contacts.click()
time.sleep(4)

contacts_button = browser.find_element_by_class_name('pl3')
contacts_button.click()
time.sleep(3)

for i in range(3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    browser.find_element_by_tag_name('body').send_keys(Keys.HOME)
    time.sleep(3)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')


followers = browser.find_elements_by_class_name('mn-connection-card__details')

followerlist=[]
for i in followers:
    followerlist.append(str(i.text))

with open('followers.txt','w',encoding='UTF-8') as file:
    for i in followerlist:
        file.write(i)
        file.write('\n')

browser.quit()