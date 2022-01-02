import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import pyplot as plt
from datetime import timedelta, date

plt.style.use('ggplot')

sticker = str(input('Enter Sticker name here').upper())
start_date = input('Enter Start Date (YYYY-MM-DD)')
end_date = date.today()

data = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)

df = pd.DataFrame(data)

data['ma_30'] = data['Adj Close'].rolling(window=30).mean()
data['ma_50'] = data['Adj Close'].rolling(window=50).mean()
data['mtsd_30'] = data['Adj Close'].rolling(window=30).std()
data['mtsd_50'] = data['Adj Close'].rolling(window=50).std()
data['above_mean'] = ma_30 = data['ma_30'] + data['mtsd_30']
data['below_mean'] = ma_30 = data['ma_30'] - data['mtsd_30']

date = data.index
closing_price = data['Adj Close']
ma_30 = data['ma_30']
ma_50 = data['ma_50']
above_mean = data['above_mean']
below_mean = data['below_mean']

print(data)

plt.plot(date, ma_30, date, ma_50, date, closing_price)
plt.title(f'Closing Price Movement of {sticker}')
plt.xlabel('Dates')
plt.ylabel('USD')
plt.grid(True)
plt.legend(["ma_30", "ma_50", "price"])
plt.show()

plt.plot(date, closing_price, date, above_mean, date, below_mean, date, ma_30)
plt.title(f'Closing Price Movement of {sticker}')
plt.xlabel('Dates')
plt.ylabel('USD')
plt.grid(True)
plt.legend(["price", "above_mean", "below_mean","ma_30"])
plt.show()
t