import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import seaborn as sns

plt.style.use('bmh')

sticker = str(input('Company Sticky').upper())
start_date = input('Enter Start Date (YYYY-MM-DD)')
end_date = input('Enter End Date (YYYY-MM-DD)')

data = yf.download(sticker, start_date, end_date)['Adj Close']
print(data.head())

daily_returns = (data/data.shift(1))-1

daily_returns.hist(bins=100, ec='black')
plt.title(f'Histogram of {sticker}\'s returns')
plt.show()

sns.distplot(daily_returns)
plt.title(f'Distribution plot of {sticker}\'s return')
plt.show()

sns.distplot(data)
plt.title(f'Distribution plot of {sticker}\'s closing price')
plt.show()

plt.plot(data)
plt.title(f'Closing Price of {sticker}')
plt.xlabel('Date')
plt.ylabel('Adj. Closing Price')
plt.show()