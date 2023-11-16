import numpy as np
import matplotlib.pyplot as plt


def worst_x_years(x):
    return year[np.argsort(x)]

to_int_list = np.vectorize(int)

data = np.loadtxt('task 3/data/populations.txt')
year, hares, lynxes, carrots = data.T

carrots_mean = np.mean(carrots)
print('mean_carrots',carrots_mean)

carrots_std = np.std(carrots)
print('std_carrots',carrots_std)

carrots_max = np.max(carrots)
print('max_carrots',carrots_max)

top2 = np.argsort(data)[:2]
print(f"Имеет наибольшую популяцию за каждый год:\n{to_int_list(year[top2])}")


print(f'{year[hares > 50000]} - over 50000 hares\n{year[lynxes > 50000]} - over 50000 lynxes\n{year[carrots > 50000]} - over 50000 carrots')


print(f'worst years for carrots:{to_int_list(worst_x_years(carrots)[:2])}')
print(f'worst years for hares:  {to_int_list(worst_x_years(hares)[:2])}')
print(f'worst years for lynxes: {to_int_list(worst_x_years(lynxes)[:2])}')


print(f'correlation_matrix:\n{np.corrcoef(hares,lynxes)}')


plt.axes([0.2, 0.1, 0.5, 0.8]) 
plt.plot(year, np.gradient(hares), year,np.gradient(lynxes)) 
plt.legend(('Hare', 'Lynx'), loc=(1.05, 0.5)) 
plt.show()
