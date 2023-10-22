import matplotlib.pyplot as plt
import datetime
import requests

def get_currency_rate(currency_code, date):
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date.strftime('%d/%m/%Y')}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode("windows-1251")
        start_tag = f"<CharCode>{currency_code}</CharCode>"
        start_index = content.find(start_tag)
        if start_index != -1:
            value_start = content.find("<Value>", start_index) + len("<Value>")
            value_end = content.find("</Value>", value_start)
            rate = float(content[value_start:value_end].replace(",", "."))
            return rate
    return None

today_d = datetime.date.today().day
today_m = datetime.date.today().month
start_date = datetime.datetime(2023, today_m - 1, today_d)
end_date = datetime.datetime(2023, today_m, today_d)
dates = [start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days + 1)]

usd_rates = []
for date in dates:
    rate = get_currency_rate("USD", date)
    if rate is not None:
        usd_rates.append(rate)
    else:
        usd_rates.append(0)

plt.plot(dates, usd_rates)
plt.xlabel("Дата")
plt.ylabel("Курс доллара США")
plt.title("Динамика курса доллара США за месяц")

plt.show()