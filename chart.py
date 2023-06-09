import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt

start=dt.datetime(2019,1,1)
end=dt.datetime.now()

data=web.DataReader('AAPL','yahoo',start,end)

print(mpf.available_styles())
mpf.plot(data,type="candle",style="yahoo")