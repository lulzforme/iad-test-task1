import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv', sep=',', encoding='utf-8', parse_dates=['Дата'], dayfirst=True)

plt.figure(figsize=(10, 6))
plt.plot(data['Дата'], data['Цена'].str.replace(',', '.').astype(float), marker='o', linestyle='-', label='Цена')
plt.title('График цен')
plt.xlabel('Доллар')
plt.ylabel('Цена')
plt.grid(True)


plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d.%m.%Y'))
plt.tight_layout()
plt.legend()
plt.show()
