import plotly
import plotly.graph_objs as go
import pandas as pd
import plotly.io as pio

df = pd.read_csv('coronavirus_us.csv')

trace1 = go.Bar(x=df.Date, y=df.Daily, name="일별")

trace2 = go.Scatter(x=df.Date, y=df.Cumulative, name="누적", visible=False)

data = [trace1, trace2]

updatemenus = list([

    dict(
        active=0,
         showactive = True,
         buttons=list([
            dict(label = "일별",
                 method = "update",
                 args = [{"visible": [True, False]}]), # hide trace2
            dict(label = "누적",
                 method = "update",
                 args = [{"visible": [False, True]}]) # hide trace1
            ]))])


layout = dict(
    height=350,
        margin={'t': 30},
        showlegend=True,
        xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1개월",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6개월",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="이번 년도",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1년",
                     step="year",
                     stepmode="backward"),
                dict(step="all",
                     label="전체 기간")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"),
              yaxis=dict(title="사용자수"),
              updatemenus=updatemenus)

fig=dict(data=data, layout=layout)

plotly.offline.plot(fig)
pio.write_html(fig, file='figure1.html', auto_open=True)