import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# Load data
df = pd.read_csv(
    "usage_time.csv", encoding='CP949')

# Create figure
fig = go.Figure()

fig.add_trace(go.Bar(x=list(df.Time), y=list(df.People), name="사용자수"))

# Set title
fig.update_layout(title_text="총 상담 시간")

fig.show()
pio.write_html(fig, file='figure7.html', auto_open=True)