import requests,os
from urllib import parse
from lxml import etree

#替换原文中的空格,cmd中空格的识别要注意
def str_replace(varstr):
    newstr=varstr.replace(' ','')
    return newstr


root_url=""
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
headers = {'User-Agent': user_agent}


"""
元素位置:
/html/body/div[1]/div[2]/div[1]/div[36]/div/div/h3/a
/html/body/div[1]/div[2]/div[1]/div[6]/div/div/h3/a
"""

for i in range(1,4):
    url="_"+str(i)+".html"
    page = requests.get(url, headers=headers)
    page.encoding = "utf-8"
    html = etree.HTML(page.text)
    linklist = html.xpath("/html/body/div[1]/div[2]/div[1]/div[6]/div/div/h3/a/@href")
    #print(linklist)
    page.encoding = "utf-8"
    html = etree.HTML(page.text)
    #title
    #print(html)
    textlist = html.xpath("//div/div/div/div/div/div/h3/a/text()")
    #print(textlist)
    for text in textlist:
        #target url
        filepath = text + ".mp3"
        file_encode=parse.quote(text)+ ".mp3"
        #print(file_encode)
        real_url=root_url+parse.quote("/")+file_encode
        filepath=str_replace(filepath)
        real_filepath= "C:\\Users\\koazy-0\\2\\"+filepath
        cmd="curl "+real_url+" -o "+real_filepath
        print(cmd)
        os.system(cmd)


