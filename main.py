import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

data = \
    {'ВТП Казани, тыс. руб.': [674739900.0, 748722900.0, 773031100.0, 798154610.75, 824094635.6, 850877711.26,
                               878531236.88],
     'Добавленная стоимость, тыс. руб.': [191057445.0, 221584931.0, 226103515.0, 230716026.71, 235422633.65,
                                          240225255.38, 245125850.59],
     'ДС Обрабатывающие производства, тыс. руб.': [75373868.0, 80169194.0, 76066267.0, 84036788.742, 83376075.288,
                                                   84464848.41, 87428640.058],
     'ДС Строительство, тыс. руб.': [8376613.0, 9553660.0, 8194075.0, 9474654.494, 9450004.969, 9404600.178,
                                     9834121.537],
     'ДС Транспортировка и хранение, тыс. руб.': [26272378.0, 35407329.0, 29875960.0, 33025890.484, 34141807.848,
                                                  33655771.175, 34993312.831],
     'ДС Оптовая и розничная торговля, тыс. руб.': [19963824.0, 25665497.0, 36181429.0, 29250150.33, 31595939.083,
                                                    33712478.953, 32791813.99],
     'ДС Деятельность в области информатизации и связи, тыс. руб.': [6646511.0, 9461344.0, 10263705.0, 9450155.787,
                                                                     10127289.203, 10359428.578, 10385280.659]}

dates = [2017 + i for i in range(7)]

# plotly start
fig = go.Figure()
for col in range(7):
    fig.add_trace(go.Scatter(x=dates,
                             visible=True))
# buttons for menu 1, names
buttons = []

# create traces for each Room_number:
for df, value in data.items():
    buttons.append(dict(method='update',
                        label=df,
                        visible=True,
                        args=[{'y': [value]}, {'visible':True}]
                        ))

updatemenu = [{'buttons': buttons, 'direction': 'down', 'showactive': True, 'y':0.6}]

fig.update_layout(showlegend=False, updatemenus=updatemenu)
fig.write_html("sheet.html")

