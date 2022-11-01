import requests
from bs4 import BeautifulSoup
import re
import os.path
from urllib import parse
from lxml import etree

root_url=
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}


"""
/html/body/div[1]/div[2]/div[1]/div[36]/div/div/h3/a
/html/body/div[1]/div[2]/div[1]/div[6]/div/div/h3/a
"""

page = requests.get("www.baidu.com", headers=headers)
page.encoding = "utf-8"
html = etree.HTML(page.text)
#title
print(html)
textlist = html.xpath("//div/div/div/div/div/div/h3/a/text()")
print(textlist)
for text in textlist:
    #target url
    filepath = text + ".mp3"
    file_encode=parse.quote(text)+ ".mp3"
    #print(file_encode)
    real_url=root_url+file_encode
    cmd="curl -L "+real_url+" -o "+filepath
    print(cmd)
    #os.system(cmd)


"""for i in range(1,4):
    url="https://www.baidu.com"+str(i)+".html"
    page = requests.get(url, headers=headers)
    page.encoding = "utf-8"
    html = etree.HTML(page.text)
    linklist = html.xpath("/html/body/div[1]/div[2]/div[1]/div[6]/div/div/h3/a/@href")
    #print(linklist)
    
    
    """


