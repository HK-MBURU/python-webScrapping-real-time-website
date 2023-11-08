from bs4 import BeautifulSoup
import requests

url='https://www.kilimall.co.ke/new/commoditysearch?c=5727&aside=&gc_id=5727'
html_text=requests.get(url).text

soup=BeautifulSoup(html_text,'lxml')

item=soup.find('div',class_='grid-content bg-purple clearfix')
print(item)