import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
from matplotlib import pyplot as plt
from datetime import timedelta, date

plt.style.use('fivethirtyeight')

sticker = str(input('Enter Sticker name here').upper())
start_date = input('Enter Start Date (YYYY-MM-DD)')
end_date = date.today()

data = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)

df = pd.DataFrame(data)

plt.plot(data['Adj Close'])
plt.legend(['Stocks'])
plt.show()