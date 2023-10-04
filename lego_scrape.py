import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for i in range(10, 24):
    url = 'https://brickset.com/sets/theme-Speed-Champions/year-20{}'.format(i)

    response = requests.get(url=url)

    soup = BeautifulSoup(response.text, 'lxml')

    tree = html.fromstring(str(soup))

    items = soup.find_all('div', class_='meta')

    for item in items:
        name = item.find('h1').text

        RRP = item.find_all('dd')[3 or 1].text.replace(' | More', '')
        # RRP.append(price)
        # if ('$' and '€') not in price:
        #     price = item.find_all('dd')[1].text
        #     RRP.append(price)

        launchExit = item.find_all('div', class_='col')[1].find('dd').text
        data.append({'Name': name, 'RRP': RRP, 'launchExit': launchExit})

df = pd.DataFrame(data)
df.to_csv('sample.csv')
