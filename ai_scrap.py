
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
keyword = "Machine Learning"
# link = 'https://www.google.com/search?q=' + keyword
current_page_url = "https://www.google.com/search?q=machine+learning&biw=1707&bih=948&tbm=nws&sxsrf=APwXEdcP3OgcyTjtOTMT4tphO7d4e7ITMQ%3A1686803266463&ei=QpOKZIzuG6q64-EPnsiF4Ao&ved=0ahUKEwiMl4Pst8T_AhUq3TgGHR5kAawQ4dUDCA0&uact=5&oq=machine+learning&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQAzILCAAQgAQQsQMQgwEyBwgAEIoFEEMyBwgAEIoFEEMyBwgAEIoFEEMyBwgAEIoFEEMyBwgAEIoFEEMyBwgAEIoFEEMyBwgAEIoFEEMyBwgAEIoFEEMyBwgAEIoFEENQAFgAYOcBaABwAHgAgAFuiAFukgEDMC4xmAEAwAEB&sclient=gws-wiz-news"
response = requests.get(current_page_url, headers=header)
soup= BeautifulSoup(response.content, 'html.parser')
list_news =[]
list_title = []
list_url = []

def scrap_page(current_page_url):
    response = requests.get(current_page_url, headers=header)
    soup= BeautifulSoup(response.content, 'html.parser')
    for obj in soup.find_all("a", {"jsname":"YKoRaf"}, href=True):
        dict_news = {}
        if obj.text.strip() not in list_title:
            list_title.append(obj.text.strip())
            list_url.append(obj['href'])
            dict_news = {"tag":"test","name": "Nicha","title":obj.text.strip(), "url":obj['href'], "keyword": "machine learning"}
            list_news.append(dict_news)
            time.sleep(0.1)

for i in range(0,30):
    current_page_url = "https://www.google.com/search?q=machine+learning&biw=667&bih=948&tbm=nws&sxsrf=APwXEdfcyxFBu8U4RMo2wOPErBlw4cZWig:1686812623867&ei=z7eKZNDHNJ_gseMP67ScoAg&start=" +str(i*10)+"&sa=N&ved=2ahUKEwiQ6_3Z2sT_AhUfcGwGHWsaB4Q4ZBDy0wN6BAgEEAY"
    scrap_page(current_page_url)
    # print(list_news)
    requests.post(url='http://10.225.194.104:2424/add-item-many/', json=list_news)


