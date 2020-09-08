import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

label_gender = ["남성", "여성"]
label_age = ["10대", "20대", "30대", "40대", "50대", "60대+"]
label_current_weight = ["30kg대", "40kg대", "50kg대", "60kg대", "70kg대", "80kg대", "90kg대", "100kg 이상"]

updatemenus = list([

    dict(
        active=0,
         showactive = True,
         buttons=list([
            dict(label = "전체고객",
                 method = "update",
                 args = [{"visible": [True, True]}]), # hide trace2
            dict(label = "상담고객",
                 method = "update",
                 args = [{"visible": [True, True]}]), # hide trace1,
            dict(label = "이탈고객",
                 method = "update",
                 args = [{"visible": [True, True]}]) # hide trace1
            ]))])

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=label_gender, textinfo='label+percent', values=[42, 58], name="성별"),
              1, 1)
fig.add_trace(go.Pie(labels=label_age, textinfo='label+percent', values=[5, 28, 38, 9, 10, 7, 3], name="나이"),
              1, 2)
fig.add_trace(go.Pie(labels=label_current_weight, textinfo='label+percent', values=[3,12,37,34,7,3,3,1], name="몸무게"),
              1, 3)
# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="이용자 통계",
    # Add annotations in the center of the donut pies.
    showlegend=False,
updatemenus=updatemenus)
fig.show()

pio.write_html(fig, file='figure2.html', auto_open=True)