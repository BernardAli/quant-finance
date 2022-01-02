import numpy as np
import pandas_datareader.data as web
from matplotlib import pyplot as plt
import seaborn as sns

sticker = str(input('Enter Stock Symbol Here').upper())

start_date = str(input('Enter Start Date Here (YYYY-MM-DD)'))
end_date = str(input('Enter End Date Here (YYYY-MM-DD)'))

data = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

daily_returns = (data/data.shift(1))-1

sns.displot(daily_returns, kde=True)
plt.show()
