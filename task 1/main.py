import time
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import datetime


def main():
    plt.ion()

    current_date_time = datetime.datetime.now()
    x = [current_date_time.strftime("%H:%M:%S")]
    y = [get_price()]

    figure, ax = plt.subplots()
    line = ax.plot(x, y)[0]

    plt.title("Exchange Rates", fontsize=20)

    plt.xlabel("Time")
    plt.ylabel("₽/$")

    while True:
        current_date_time = datetime.datetime.now()
        x.append(current_date_time.strftime("%H:%M:%S"))
        y.append(get_price())
        line.set_xdata(x)
        line.set_ydata(y)

        ax.relim()
        ax.autoscale_view(True, True, True)

        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(10)


def get_price():
    html_data = requests.get(
        'https://ru.investing.com/currencies/usd-rub-historical-data').text
    soup = BeautifulSoup(html_data, 'html.parser')

    return float(soup.find('span', class_="text-2xl").get_text().replace(',', '.'))


if __name__ == '__main__':
    main()
