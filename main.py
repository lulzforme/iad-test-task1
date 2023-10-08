import matplotlib.pyplot as plt
import numpy as np

from parse import parse_date_array_and_valutes_change

url = "https://www.cbr-xml-daily.ru/daily_json.js"

### DATA FILLING ###
accepted_valutes = ["USD", "EUR", "AUD"]
date_array, datas_valutes_change = parse_date_array_and_valutes_change(dates_quantity=5, url=url,
                                                                   accepted_valutes=accepted_valutes)
### DATA FILLING ###
### GRAPH STUFF ###
ax = plt.figure().add_subplot(projection='3d')

list_datas_valutes_change = list(datas_valutes_change.values())
list_datas_valutes_name = list(datas_valutes_change.keys())
for i in range(len(datas_valutes_change)):
    axis_y_dates = np.arange(len(date_array)) # TODO вывести названия
    axis_x_valute_position = np.arange(len(date_array))
    axis_x_valute_position[...] = i
    axis_z_valute_points = list_datas_valutes_change[i]

    ax.plot(axis_x_valute_position, axis_y_dates, axis_z_valute_points)

    ax.text(i, 0, 0, list_datas_valutes_name[i])

for i in range(len(date_array)):
    ax.text(x=0, y=i, z=-2, s=date_array[i])

ax.set_xlabel("POSITION")
ax.set_ylabel("DATE")
ax.set_zlabel("VALUE")

plt.show()
### GRAPH STUFF ###
