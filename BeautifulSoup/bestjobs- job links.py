import requests
from bs4 import BeautifulSoup

headers_param={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

glasdor = requests.get('https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm',headers=headers_param)

soup=BeautifulSoup(glasdor.content,'html.parser')

views=soup.find_all('div',{'class':'col-12 col-lg-2'})
list1=[]
for view in views:
    list1.append(str(view.a))

list1.remove(list1[0])

links=[]
for i in list1:
    i=i.replace('<a class="" href="','')
    last=i.rindex("htm")
    links.append(i[0:last+3])

print(links[0])
print(len(links))

import pandas
df = pandas.DataFrame(data={"JobLinks": links})
#df.to_csv("JObLinks.csv")
print(df)