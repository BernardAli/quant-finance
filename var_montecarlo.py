import numpy as np
import pandas as pd
from scipy.stats import norm
import pandas_datareader.data as web
import datetime
import math


class ValueAtRiskMonteCarlo:

    def __init__(self, S, mu, sigma, c, n, iterations):
        self.S = S
        self.mu = mu
        self.sigma = sigma
        self.c = c
        self.n = n
        self.iterations = iterations


    def simulation(self):
        stock_date = np.zeros([self.iterations, 1])
        rand = np.random.normal(0, 1, [1, self.iterations])

        # equation for the S(t) stock price
        stock_price = self.S*np.exp(self.n*(self.mu - 0.5*self.sigma**2) + self.sigma*np.sqrt(self.n) * rand)

        # we have to sort the stock price to determine the percentile
        stock_price = np.sort(stock_price)

        # it depends on the confidence level: 95% -> 5 and 99% -> 1
        percentile = np.percentile(stock_price, (1-self.c)*100)

        return self.S-percentile


if __name__ == "__main__":
    S = 1e6     # this is the investment (stocks or whatever)
    c = 0.90    # confidence level : this is 99%
    n = 1       # 1 day
    iterations = 1000000        # number of paths in the Monte-Carlo simulation

    # historical data to approximate mean and standard deviation
    sticker = str(input('Enter sticker here').upper())

    start_date = datetime.datetime(2014, 1, 1)
    end_date = datetime.datetime.today()

    # download stock related data from yahoo finance
    sticker = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)

    # we can use pct_change() to calculate daily returns
    sticker['returns'] = sticker['Adj Close'].pct_change()

    # we can assume daily returns to be normally distributed: mean and variance (std)
    # can describe the process
    mu = np.mean(sticker['returns'])
    sigma = np.std(sticker['returns'])

    model = ValueAtRiskMonteCarlo(S, mu, sigma, c, n, iterations)

    print('Value at risk with Monte-Carlo simulation', model.simulation())