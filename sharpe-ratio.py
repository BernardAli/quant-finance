import numpy as np
import pandas_datareader.data as web
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import seaborn as sns

plt.style.use('bmh')

sticker = str(input('Company Ticker').upper())
start_date = input('Enter Start Date (YYYY-MM-DD)')
end_date = input('Enter End Date (YYYY-MM-DD)')
risk_free_return = float(input('Enter risk free return'))

data = web.DataReader(sticker, start=start_date, end=end_date, data_source='yahoo')['Adj Close']

daily_returns = (data/data.shift(1))-1

plt.plot(daily_returns)
plt.legend(['Percentage Daily Returns'])
plt.title(f'{sticker} daily percentage returns')
plt.show()

sns.displot(daily_returns, kde=True)
plt.show()

average_return = daily_returns.mean()
std_return = daily_returns.std()

sharpe_ratio = (average_return - risk_free_return) / std_return
print(sharpe_ratio)