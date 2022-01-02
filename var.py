import numpy as np
import pandas as pd
from scipy.stats import norm
import pandas_datareader.data as web
import datetime

# if we want to calculate VaR for tomorrow
def value_at_risk(position, c, mu, sigma):
    alpha = norm.ppf(1-c)
    var = position * (mu-sigma*alpha)
    return var

# we want to calculate VaR in the n days time
# we have to consider that the mean and standard deviation will change
# mu = mu*n sigma=sigma*sqrt(n), we have to use these transformation

def value_at_risk_long(S, c, mu, sigma, n):
    alpha = norm.ppf(1-c)
    var = S * (mu * n-sigma * alpha*np.sqrt(n))
    return var

if __name__ == "__main__":

    # historical data to approximate mean and standard deviation
    sticker = str(input('Enter sticker here').upper())

    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.today()

    # download stock related data from Yahoo finance
    sticker = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)

    # we can use pct_change() to calculate daily returns
    sticker['returns'] = sticker['Adj Close'].pct_change()

    S = 100     # this is the investment (stocks or whatever)
    c = 0.99    # confidence level: this is it 99%

    # we can assume daily returns to be normally distributed: mean and variance (std)
    # can describe the process
    mu = np.mean(sticker['returns'])
    sigma = np.std(sticker['returns'])

    print('Value at risk is: $%0.2f' % value_at_risk(S, c, mu, sigma))
