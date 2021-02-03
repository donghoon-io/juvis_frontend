import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

type_data=[[1000]*31]*9
label_data=["모듈 1", "모듈 2", "모듈 3", "모듈 4", "모듈 5", "모듈 6", "모듈 7", "모듈 8", "모듈 9", "모듈 10",
            "모듈 11", "모듈 12", "모듈 13", "모듈 14", "모듈 15", "모듈 16", "모듈 17", "모듈 18", "모듈 19", "모듈 20",
            "모듈 21", "모듈 22", "모듈 23", "모듈 24", "모듈 25", "모듈 26", "모듈 27", "모듈 28", "모듈 29", "모듈 30",
            "모듈 31"]

updatemenus = list([
    dict(
        active=0,
         showactive = True,
         buttons=list([
            dict(label = "전체고객",
                 method = "update",
                 args = [{"visible": [True, False, False, False, False, False, False, False, False]}]), # hide trace2
            dict(label = "상담고객",
                 method = "update",
                 args = [{"visible": [False, True, False, False, False, False, False, False, False]}]), # hide trace1,
            dict(label = "이탈고객",
                 method = "update",
                 args = [{"visible": [False, False, True, False, False, False, False, False, False]}]), # hide trace1,
            dict(label = "유형1",
                 method = "update",
                 args = [{"visible": [False, False, False, True, False, False, False, False, False]}]), # hide trace1, # hide trace1,
            dict(label = "유형2",
                 method = "update",
                 args = [{"visible": [False, False, False, False, True, False, False, False, False]}]), # hide trace1, # hide trace1,
            dict(label = "유형3",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, True, False, False, False]}]), # hide trace1, # hide trace1,
            dict(label = "유형4",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, False, True, False, False]}]), # hide trace1,
            dict(label = "유형5",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, False, False, True, False]}]), # hide trace1,
            dict(label = "기타",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, False, False, False, True]}]) # hide trace1
            ]))])

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])


for (index, item) in enumerate(type_data):
    fig.add_trace(go.Bar(x=label_data, y=item, name="모듈"))


fig.update_layout(
    title_text="이용자 통계",
    # Add annotations in the center of the donut pies.
    showlegend=False,
updatemenus=updatemenus)
fig.show()

pio.write_html(fig, file='figure3.html', auto_open=True)
