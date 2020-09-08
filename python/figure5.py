import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# Load data
df = pd.read_csv(
    "connection.csv", encoding='CP949')

# Create figure
fig = go.Figure()

fig.add_trace(go.Bar(x=list(df.Type), y=list(df.Percentage), name="사용률1"))

# Set title
fig.update_layout(title_text="방문 상담 연결률")

fig.layout.yaxis.tickformat = ',.0%'
fig.layout.yaxis.range = [0 ,1]

fig.show()
pio.write_html(fig, file='figure5.html', auto_open=True)