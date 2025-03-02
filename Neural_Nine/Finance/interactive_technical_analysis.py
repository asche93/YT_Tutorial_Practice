# Interactive Technical Analysis Tool in Python (SMA, RSI, BBANDS)
# In this video we build an interactive and customizable technical analysis tool in Python.
# TA-Lib: https://pypi.org/project/TA-Lib/
# https://www.youtube.com/watch?v=3HP-YbFuL5U

import plotly.graph_objs as go
import plotly.io as pio
import talib as ta
import yfinance as yf
from plotly.subplots import make_subplots

# Set rendering in browser
pio.renderers.default = "browser"

# Stock we wanne download, e.g. Apple
ticker = "BTC-USD"
start_date = "2022-01-01"
end_date = "2023-01-01"

# Download data
df = yf.download(ticker, start_date, end_date)

# Introduce Simple moving average
df["SMA"] = ta.SMA(df["Close"], timeperiod=20)
# Introduce Relative strength index
df["RSI"] = ta.RSI(df["Close"], timeperiod=14)
# Broad band
# nbdevdn: standard deviation down, mattype: moving average type
df["Upper_BB"], df["Middle_BB"], df["Lower_BB"] = ta.BBANDS(
    df["Close"], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0
)

fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.2,
    row_heights=[0.7, 0.3],
    subplot_titles=[f"{ticker} Price and Indicators", "RSI"],
)

# Set candlestick properties
candlestick = go.Candlestick(
    x=df.index, open=df.Open, high=df.High, low=df.Low, close=df.Close, name="Price"
)


sma_line = go.Scatter(
    x=df.index,
    y=df.SMA,
    line={"color": "blue", "width": 2},
)

upper_bb = go.Scatter(
    x=df.index, y=df["Upper_BB"], line={"color": "red", "width": 1}, name="Upper BB"
)


lower_bb = go.Scatter(
    x=df.index, y=df["Lower_BB"], line={"color": "red", "width": 1}, name="Lower BB"
)


middle_bb = go.Scatter(
    x=df.index, y=df["Middle_BB"], line={"color": "red", "width": 1}, name="Middle BB"
)

# Add component to upper section of plot
fig.add_trace(candlestick, row=1, col=1)
fig.add_trace(sma_line, row=1, col=1)
fig.add_trace(upper_bb, row=1, col=1)
fig.add_trace(lower_bb, row=1, col=1)
fig.add_trace(middle_bb, row=1, col=1)


rsi = go.Scatter(x=df.index, y=df.RSI, line={"color": "purple", "width": 2}, name="RSI")


fig.add_trace(rsi, row=2, col=1)


mark30 = go.layout.Shape(
    type="line",
    x0=df.index[0],
    y0=30,
    x1=df.index[-1],
    y1=30,
    line={"color": "gray", "width": 1, "dash": "dash"},
)

mark70 = go.layout.Shape(
    type="line",
    x0=df.index[0],
    y0=70,
    x1=df.index[-1],
    y1=70,
    line={"color": "gray", "width": 1, "dash": "dash"},
)

fig.add_shape(mark30, row=2, col=1)
fig.add_shape(mark70, row=2, col=1)


# Layout update
fig.update_layout(
    # Overall title
    title=f"{ticker} Technical Analysis",
    yaxis_title="Price",
    xaxis_title="Date",
    xaxis_rangeslider_visible=False,
    height=800,
    template="plotly_dark",
    legend=dict(
        font=dict(color="white"),
        bgcolor="rgba(0,0,0,0.5)",
        bordercolor="white",
        borderwidth=1,
    ),
)


fig.update_yaxes(range=[0, 100], row=2, col=1)

fig.show()
