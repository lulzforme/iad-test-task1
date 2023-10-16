from zeep import Client
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

date_from = input("Введите начальную дату в формате yyyy-MM-dd:")
date_to = input("Введите конечную дату в формате yyyy-MM-dd:")

client = Client('http://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?wsdl')
response = client.service.GetCursDynamicXML(f'{date_from}-00:00', f'{date_to}-00:00', 'R01235')

array_x = []
array_y = []
for temp in iter(response):
    array_x.append(datetime.fromisoformat(temp[0].text).strftime('%d-%m-%Y'))
    array_y.append(float(temp[3].text))

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(array_x, array_y)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

plt.xticks(rotation=45)
plt.xlabel("Дата", fontsize=20)
plt.ylabel("Стоимость (₽)", fontsize=20)
plt.title(f"Курс рубля к доллару \n "
          f"от:{date_from} до: {date_to}", fontsize=23)
plt.show()
