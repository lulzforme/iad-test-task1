import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

if __name__ == '__main__':
    request = requests.get('https://ru.investing.com/currencies/usd-rub-historical-data')
    prices = dict()
    soup = BeautifulSoup(request.text, 'html.parser')
    items = soup.find_all('tr', {"class": 'datatable_row__Hk3IV'})[8:30]
    for item in items:
        if item.find('time') is not None:
            data = item.find('time').text
            currency = item.find('td', {"class": 'datatable_cell__LJp3C datatable_cell--align-end__qgxDQ'}).text
            currency = float(currency.replace(",", "."))
            prices[data] = currency
    x = [i for i in range(1, len(items) + 1)]
    dates = list(reversed(list(prices.keys())))
    y = list(reversed(list(prices.values())))
    plt.figure(figsize=(20, 10))
    plt.xticks(ticks=x, labels=dates, rotation=90)
    plt.plot(x, y)
    plt.show()


