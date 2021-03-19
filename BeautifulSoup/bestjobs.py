import requests
from bs4 import BeautifulSoup

headers_param={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
#glasdor = requests.get('https://www.glassdoor.com/List/Best-Jobs-in-America-LST_KQ0,20.htm',headers=headers_param)
glasdor = requests.get('https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm',headers=headers_param)


#print(glasdor.status_code)

#print(glasdor.content)

jobs = glasdor.content

soup = BeautifulSoup(jobs,'html.parser')

#print(soup.title)

"""
print(soup.find("h1"))
print(soup.find("h1").text[0:15])
print(soup.find("h1").text)
a = soup.find("h1").text
print(a[0:15])
"""
#print(soup.find("div"))
#print(soup.find_all("div"))
#print(soup.find_all("a"))
#print(soup.find_all("p"))

#print(soup.find_all("p",{'class':'h2 m-0 entryWinner pb-std pb-md-0'}))

all_jobs = soup.find_all("p",{'class':'h2 m-0 entryWinner pb-std pb-md-0'})

for job in all_jobs:
    #print(job.a)
    print(job.a.text)

all_data = soup.find_all("div",{'class':'col-6 col-lg-4 dataPoint'})

for data in all_data:
    #print(data)
    print(data.text)