import matplotlib.pyplot as plt
import pandas as pd

#Даты начала и конца периода
print("Введите дату начала периода: ")
start_date = input()
print("Введите дату конца периода: ")
end_date = input()

#Запрос данных о курсе доллара
url = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start_date}&date_req2={end_date}&VAL_NM_RQ=R01235'
df = pd.read_xml(url, encoding='cp1251')

#Даты и курсы из загруженных данных
dates = df['Date'].tolist()
rates = df['Value'].tolist()
data_length = len(df)

#Преобразование курсов в числовой формат
parsed_rates = []
shortened_dates = []

for i in range(0, data_length):
    parsed_rates.append(float(rates[i].replace(",", ".")))
    shortened_dates.append(dates[i][0:5])

#Максимальное и минимальное значение и их индексы
max_rate = max(parsed_rates)
min_rate = min(parsed_rates)
max_index = parsed_rates.index(max_rate)
min_index = parsed_rates.index(min_rate)

#График курса доллара
plt.figure(figsize=(15, 6))
plt.plot(shortened_dates, parsed_rates, color='red')  # Изменение цвета на красный
plt.grid(True)
plt.xlabel("Дата")
plt.ylabel("Курс")
plt.xticks(rotation=45)

#Точки с максимальным и минимальным значениями на графике
plt.scatter(shortened_dates[max_index], max_rate, color='green', label=f'Max: {max_rate}', marker='^', s=100)
plt.scatter(shortened_dates[min_index], min_rate, color='blue', label=f'Min: {min_rate}', marker='v', s=100)

title = f"Курс доллара за период с {start_date} по {end_date}"
plt.title(title)

plt.show()
