import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter

headers_param={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

glasdor = requests.get('https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm',headers=headers_param)

jobs = glasdor.content

soup = BeautifulSoup(jobs,'html.parser')

all_data = soup.find_all("div",{'class':'col-6 col-lg-4 dataPoint'})

i=0
datas=[]
for data in all_data:
    datas.append(data.text.strip().partition(" "))


j=0
salary=[]
satisfaction=[]
jobopennings=[]
for j in range(0,len(all_data),3):
    salary.append(datas[j][0])
    satisfaction.append(datas[j+1][0].partition('/')[0])
    jobopennings.append(datas[j+2][0])

salary=[i.replace('$','') for i in salary]

d = {'salary': salary, 'satisfaction': satisfaction, 'jobopennings':jobopennings}
df = pd.DataFrame(data=d)
print(df)

#df.to_csv('best_jobs_in_america.csv')
#df.to_excel('best_jobs_in_america.xlsx', engine='xlsxwriter')
