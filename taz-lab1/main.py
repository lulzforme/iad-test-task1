import matplotlib
import matplotlib.pyplot as plt
import requests
import datetime
from matplotlib.dates import DateFormatter


def draw_graph(currency_col: list[dict]) -> None:
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xlabel("Дата")
    ax.set_ylabel("Курс доллара")
    ax.set_zlabel("Изменение")

    ax.xaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))

    x = []
    y = []
    z = []

    for item in currency_col:
        x.append(item.get("date"))
        y.append(item.get("usd"))
        z.append(item.get("delta"))

    x_dates = matplotlib.dates.date2num(x)
    ax.plot(x_dates, y, z)
    plt.show()


def get_extended_usd_list(currency_col: list[dict]) -> list[dict]:
    new_col = []
    next_item = None
    length = len(currency_col)
    key = "usd"
    for index, current_item in enumerate(currency_col):
        if index < (length - 1):
            next_item = currency_col[index + 1]

        prev_usd = current_item[key]
        current_usd = next_item[key]
        new_col.append({**current_item, "delta": (prev_usd - current_usd) / current_usd * 100})

    return new_col


def get_usd_list(prepared_dates: list) -> list[dict]:
    col = []
    for current_date in prepared_dates:
        prepared_link = 'https://www.cbr-xml-daily.ru/archive/{}/{}/{}/daily_json.js'

        month = '0' + str(current_date.month) if current_date.month < 10 else current_date.month
        day = '0' + str(current_date.day) if current_date.day < 10 else current_date.day

        link = prepared_link.format(current_date.year, month, day)
        current_request = requests.get(link)
        current_parsed_request = current_request.json()
        usd = current_parsed_request['Valute']['USD']['Value']

        col.append({"date": current_date, "usd": usd})

    return col


def get_dates() -> list[datetime]:
    count = 14
    these_dates = []
    date = datetime.datetime.today()

    for i in range(count):
        prev_date = date - datetime.timedelta(days=1)
        date = prev_date

        if prev_date.weekday() == 0 or prev_date.weekday() == 6:
            continue

        these_dates.append(prev_date.date())

    return these_dates


if __name__ == '__main__':
    dates = get_dates()
    base_collection = get_usd_list(dates)
    prepared_collection = get_extended_usd_list(base_collection)
    draw_graph(prepared_collection)
