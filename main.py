import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

url = 'https://ru.investing.com/currencies/usd-rub-historical-data'
request = requests.get(url)

soup = BeautifulSoup(request.text, 'lxml')
items = soup.find_all('tr', class_='datatable_row__Hk3IV')
items = items[8:31]
items.reverse()

PriceDictionary = {}

for item in items:
    if item != None:
        data = item.find('td', class_='datatable_cell__LJp3C font-bold').find('time').text
        currency = item.find('td',
                             class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ datatable_cell--down___c4Fq')
        if currency == None:
            currency = item.find('td',
                                 class_='datatable_cell__LJp3C datatable_cell--align-end__qgxDQ datatable_cell--up__hIuZF')
        PriceDictionary[data] = currency.text

width = 0
x_list = []
y_list = []
data_list = []
i = 0
for data in PriceDictionary:
    data_list.append(data[:5])
    i += 2
    x_list.append(i)
    price_str = float(PriceDictionary[data].replace(",", "."))
    y_list.append(float(price_str))

x_indexes = np.arange(len(x_list))

plt.title('exchange rate with historical interval')
plt.xticks(x_indexes, data_list)
plt.xlabel('days')
plt.ylabel('exchange rate, ₽')
plt.grid(True)

plt.plot(x_indexes - (width / 2), y_list, marker='^')
plt.show()
