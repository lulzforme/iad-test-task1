import pandas as pd
import plotly.express as px

data = pd.read_csv('data.csv', sep=',', encoding='utf-8', parse_dates=['Дата'], dayfirst=True)
data['Цена'] = data['Цена'].str.replace(',', '.').astype(float)

fig = px.scatter_3d(data, x='Дата', y='Цена', z=data.index, color=data.index, text=data['Изм. %'])
fig.update_traces(marker=dict(size=5),
                  selector=dict(mode='markers+text', textposition='bottom center'))
fig.update_layout(scene=dict(xaxis_title='Дата', yaxis_title='Цена', zaxis_title='Изм. %'),
                  title='3D dollar data')

fig.show()
