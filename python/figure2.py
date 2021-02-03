import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

label_gender = ["남성", "여성"]
label_age = ["10대", "20대", "30대", "40대", "50대", "60대+"]
label_current_weight = ["30kg대", "40kg대", "50kg대", "60kg대", "70kg대", "80kg대", "90kg대", "100kg 이상"]
label_client_category = ["기타", "유형1", "유형2", "유형3", "유형4", "유형5"] # yj add


gender_data=[[42,58],[35,65],[40,60],[15,85],[50,50],[70,30],[80,20],[74,26],[35,65],[4,96]]
age_data=[[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3],[5, 28, 38, 9, 10, 7, 3]]
weight_data=[[3,12,37,34,7,3,3,1],[8,12,37,34,7,3,3,1],[3,4,37,34,7,3,3,1],[3,12,8,34,7,3,3,1],[3,12,37,34,7,3,3,1],[3,12,37,34,7,3,3,1],[3,12,37,34,7,3,3,1],[3,12,37,34,7,3,3,1],[3,12,37,34,7,3,3,1]]
type_data=[[23,12,27,22,7,9],[23,12,27,22,7,9],[23,12,27,22,7,9],[23,12,27,22,7,9],[23,12,27,22,7,9],[23,12,27,22,7,9],[23,12,27,22,7,9],[23,12,27,22,7,9],[23,12,27,22,7,9]]


updatemenus = list([

    dict(
        active=0,
         showactive = True,
         buttons=list([
            dict(label = "전체고객",
                 method = "update",
                 args = [{"visible": [True, False, False, False, False, False, False, False, False]*4}]), # hide trace2
            dict(label = "상담고객",
                 method = "update",
                 args = [{"visible": [False, True, False, False, False, False, False, False, False]*4}]), # hide trace1,
            dict(label = "이탈고객",
                 method = "update",
                 args = [{"visible": [False, False, True, False, False, False, False, False, False]*4}]), # hide trace1,
            dict(label = "유형1",
                 method = "update",
                 args = [{"visible": [False, False, False, True, False, False, False, False, False]*4}]), # hide trace1, # hide trace1,
            dict(label = "유형2",
                 method = "update",
                 args = [{"visible": [False, False, False, False, True, False, False, False, False]*4}]), # hide trace1, # hide trace1,
            dict(label = "유형3",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, True, False, False, False]*4}]), # hide trace1, # hide trace1,
            dict(label = "유형4",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, False, True, False, False]*4}]), # hide trace1,
            dict(label = "유형5",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, False, False, True, False]*4}]), # hide trace1,
            dict(label = "기타",
                 method = "update",
                 args = [{"visible": [False, False, False, False, False, False, False, False, True]*4}]) # hide trace1
            ]))])

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=4, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])


for item in gender_data:
    fig.add_trace(go.Pie(labels=label_gender, textinfo='label+percent', values=item, name="성별"),
              1, 1)
for item in age_data:
    fig.add_trace(go.Pie(labels=label_age, textinfo='label+percent', values=item, name="나이"),
              1, 2)
for item in weight_data:
    fig.add_trace(go.Pie(labels=label_current_weight, textinfo='label+percent', values=item, name="몸무게"),
              1, 3)
for item in type_data:
    fig.add_trace(go.Pie(labels=label_client_category, textinfo='label+percent', values=item, name="유형"),
              1, 4) # yj add
# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="이용자 통계",
    # Add annotations in the center of the donut pies.
    showlegend=False,
updatemenus=updatemenus)
fig.show()

pio.write_html(fig, file='figure2.html', auto_open=True)
