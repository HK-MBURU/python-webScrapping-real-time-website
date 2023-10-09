from bs4 import BeautifulSoup
with open('index.html','r') as html_file:
    content=html_file.read()
    # print(content) 
    soup=BeautifulSoup(content,'lxml')
    # print(soup.prettify)
    tags=soup.find_all('a')
    for tag in tags:
        print(tag.text)
    # print(tags)