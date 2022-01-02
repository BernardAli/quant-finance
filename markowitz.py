import numpy as np
import pandas as pd
import pandas_datareader.data as web
from matplotlib import pyplot as plt
import datetime
import seaborn as sns


plt.style.use('bmh')

sticker = ['AAPL', 'MSFT', "GE", "DB", "TSLA", "AMD", "BA"]
start_date = input("Enter start date (YYYY-MM-DD)")
end_date = input("Enter end date (YYYY-MM-DD)")

data = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

# Printing the data
print(data.head())

# The covariance of the data involve
cov = data.cov()
print(cov)

sns.heatmap(cov, annot=True)
plt.show()


# The correlation co-efficient of the data
corr = data.corr()
print(corr)

sns.heatmap(corr, annot=True)
plt.show()


data.plot(figsize=(10, 5))
plt.title('Shares')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')
plt.show()