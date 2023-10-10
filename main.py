import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import requests
from parse import get_info

btw=1; ##интервал по кол-ву месяцев
day = datetime.date.today().day
month = datetime.date.today().month
start = datetime.datetime(2023, month - btw, day)
end = datetime.datetime(2023, month, day)

date_list = []
current_date = start

while current_date <= end: ##создание листа дат графика по оси Ox
    date_list.append(current_date.date())
    current_date += datetime.timedelta(days=1) ##timedelta = добавлять или вычитать недели, дни, часы, минуты, секунды, микросекунды и миллисекунды из заданных даты и времени.

val_rates = []
val = "KZT";
for date in date_list: ##
    rate = get_info(val, date) ##выделенная функция в parse (получение данных)
    if rate is not None:
        val_rates.append(rate) ## append = добавляет элемент в конец списка или другой последовательности.
    else:
        val_rates.append(0)

fig, ax = plt.subplots() ##subplots = метод библиотеки matplotlib для настройки параметров фигуры и каждого графика соответственно
plt.subplots_adjust(top=0.89, bottom=0.115, left=0.05, right=0.99, hspace=0.2, wspace=0.2) ##параметры экрана графика для корректного отображения дат по оси Ox
ax.plot(date_list, val_rates)
ax.set_title(f"Динамика курса валюты {val}")
##ax.set_xlabel('Дата')
ax.set_ylabel(f"Курс {val}")
plt.show()