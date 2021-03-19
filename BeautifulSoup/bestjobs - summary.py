import requests
from bs4 import BeautifulSoup

headers_param={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

glasdor = requests.get('https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm',headers=headers_param)

jobs = glasdor.content

soup = BeautifulSoup(jobs,'html.parser')

##########################################################################
all_jobs = soup.find_all("p",{'class':'h2 m-0 entryWinner pb-std pb-md-0'})

for job in all_jobs:
    print(job.a.text)
##########################################################################
all_data = soup.find_all("div",{'class':'col-6 col-lg-4 dataPoint'})

for data in all_data:
    print(data.text)

