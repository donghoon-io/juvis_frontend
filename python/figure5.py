import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# Load data
df = pd.read_csv(
    "overview_inflow.csv", encoding='CP949')

# Create figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=list(df.Hour), y=list(df.Total), name="사용률1"))
fig.add_trace(go.Scatter(x=list(df.Hour), y=list(df.Book), name="사용률2"))

# Set title
fig.update_layout(
    title_text="시간대별 사용률"
)

# Add range slider
fig.update_layout(
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
        )
    )
)

fig.show()
pio.write_html(fig, file='figure5.html', auto_open=True)