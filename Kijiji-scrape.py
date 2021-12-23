import os
import re
import lxml
import requests
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup

data=[]

for i in range(1,100):
    url = f"https://www.kijiji.ca/b-tool/ottawa/page-{str(i)}/c110l1700185"
    print(url)
    scrape = requests.get(url)
    headers={"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}

    html = scrape.content
    soup = BeautifulSoup(html,'lxml')

    items = soup.find_all("div", class_="info-container")

    for item in items:
        title = item.find("div", class_="title").text.replace('\n','').replace(' ','')
        description = item.find("div", class_="description").text.replace('\n','').replace(' ','')
        price = item.find("div", class_="price").get_text().replace('\n','').replace(' ','')
        id = item.find("a").get("href").split('/')[4]
        link = "https://www.kijiji.ca"+item.find("a").get("href")

        products = {"Title": title, "Description": description, "Price": price, "ID": id, "Link": link}
    
        data.append(products)
        sleep(2)

df = pd.DataFrame(data)
df.to_csv('scrape_kijiji.csv')
