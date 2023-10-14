

# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def PlotCurrencyHistory(Valute):
#     x = np.linspace(0,10,50)
#     y = x*x+5
#     plt.figure(figsize=(12, 6))
#     plt.title(f'История курса валюты {Valute}')
#     plt.xlabel('Дата')
#     plt.xticks(rotation=45)
#     plt.ylabel('Курс')
#     plt.grid(True)
#     plt.tight_layout()
#     plt.plot(x,y)
#     plt.show()
#
# PlotCurrencyHistory("USD")



import matplotlib.pyplot as plt
import pandas as pd

print("Введите дату начала периода: ")
dateStart = input()
print("Введите дату конца периода: ")
dateEnd = input()
url = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1='+dateStart+'&date_req2='+dateEnd+'&VAL_NM_RQ=R01235'
df=pd.read_xml(url, encoding='cp1251')
print(df.head(30))
dates = df['Date'].tolist()
rates = df['Value'].tolist()
dlina=len(df)
rates2 = []
dates2 = []
for i in range(0, dlina):
    rates2.append(float(rates[i].replace(",", ".")))
    dates2.append(dates[i][0:5])
plt.figure(figsize=(15, 6))
plt.plot(dates2, rates2)
plt.grid(True)
plt.xticks(rotation=45)
plt.xlabel("Дата")
plt.ylabel("Курс")
title = "Курс доллара за период с "+dateStart+" по "+dateEnd
plt.title(title)
plt.show()