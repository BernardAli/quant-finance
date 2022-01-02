# Numbers Library
import numpy as np
import pandas as pd

# Visualization Library
from matplotlib import pyplot as plt
import seaborn as sns

# Data Library
import pandas_datareader.data as web

# Stocks to be included in our portfolio
tickers = ['MSFT', 'GE', 'BA', 'INTC', 'TSLA']

# Stocks weight
weight = [0.25, 0.20, 0.20, 0.25, 0.10]

# tickers downloads with the start and end date
price_data = web.DataReader(tickers, start='2018-01-01', end='2020-11-24', data_source='yahoo')
print(price_data.head())

price_data = price_data['Adj Close']

plt.plot(price_data)
plt.legend(tickers)
plt.show()

return_data = price_data.pct_change()[1:]
print(return_data.head())

corr = return_data.corr()
sns.heatmap(corr, annot=True)
plt.show()

weighted_returns = (weight * return_data)
print(weighted_returns.head())

port_returns = weighted_returns.sum(axis=1)
cumulative_returns = (port_returns + 1).cumprod()
print(cumulative_returns.head())


# Visualizing Cumulative Returns
plt.plot(cumulative_returns)
plt.grid(True)
plt.title('Portfolio returns')
plt.xlabel('Date')
plt.ylabel('portfolio returns')
plt.show()