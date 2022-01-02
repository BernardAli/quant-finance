import numpy as np
import pandas as pd
import pandas_datareader.data as web
from matplotlib import pyplot as plt
import datetime
import scipy.optimize as optimization

plt.style.use('seaborn')

sticker = ['AAPL', 'WMT', 'TSLA', 'GE', 'FB']
start_date = '01/01/2020'
end_date = '07/07/2020'

# downloading the data from Yahoo! Finance
def download_data(sticker):
    data = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']
    data.columns = sticker
    return data

def show_data(data):
    data.plot(figsize=(10, 5))
    plt.show()

# We usually use natural logarithm for normalization purposes
def calculate_returns(data):
    returns = np.log(data/data.shift(1))
    return returns

def plot_daily_returns(returns):
    returns.plot(figsize=(10, 5))
    plt.show()

# print out mean and covariance of stockes within [start_date, end_date]. There are 252 trading days within a year
def show_statistics(returns):
    print(returns.mean()*252)
    print(returns.cov()*252)
    print(returns.corr()*252)

# weights defines what stocks to include (with what portion) in the portfolio
def initialize_weights():
    weights = np.random.random(len(sticker))
    weights /= np.sum(weights)
    print(weights)
    return weights

# expected portfolio return
def calculate_portfolio_return(returns, weights):
    portfolio_return = np.sum(returns.mean()*weights)*252
    print("Expected portfolio return: ", portfolio_return)

# expected portfolio std
def calculate_portfolio_variance(returns, weights):
    portfolio_variance = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*252, weights)))
    print("Expected variance: ", portfolio_variance)


# Monte-Carlo simulation
def generate_portfolios(weights, returns):
    preturns = []
    pvariances = []

    # Monte-Carlo simulation: we generate several random weights -> so random portfolios !!!
    for i in range(10000):
        weights = np.random.random(len(sticker))
        weights /= np.sum(weights)
        preturns.append(np.sum(returns.mean()*weights)*252)
        pvariances.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov()*252, weights))))

    preturns = np.array(preturns)
    pvariances = np.array(pvariances)
    print(f"Pretruns is {preturns}")
    print(f"pvariances is {pvariances}")
    return preturns, pvariances


def plot_portfolios(returns, variances):
    plt.figure(figsize=(10, 6))
    plt.scatter(variances, returns, c=returns/variances, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()

# Ok this is the result of the simulation.. we have to find the optimal portfolio with
# some optimization techniques

def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean()*weights)*252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*252, weights)))
    return np.array([portfolio_return, portfolio_volatility, portfolio_return/portfolio_volatility])

# [means] that we want to maximize according to the Sharpe-ration
# note: maximizing f(x) function is the same as minimizing -f(x) !!!

def min_func_sharpe(weights, returns):
    returns - statistics(weights, returns)[2]

# what are the constraints? The sum of the wights = 1 !!! f(x) =0, this is the function to minimize
def optimize_portfolio(weights, returns):
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x)-1})
    bounds = tuple((0, 1) for x in range(len(sticker)))
    optimum = optimization.minimize(fun=min_func_sharpe, x0=weights, args=returns, method='SLSQP',
                                    bounds=bounds, constraints=constraints)
    return optimum

# optimal portfolio according to weights: 0 means no shares of that given company
def print_optimal_portfolio(optimum, returns):
    print("Optimal weights: ", optimum['x'].round(3))
    print("Expected return, volatility and sharpe ratio: ", statistics(optimum['x'].round(3), returns))

def show_optimal_portfolio(optimum, returns, preturns, pvariances):
    plt.figure(figsize=(10, 6))
    plt.scatter(pvariances, preturns, c=preturns/pvariances, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Retrun')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(optimum['x'], returns)[1], statistics(optimum['x'], returns)[0], 'g*', markersize=20.0)
    plt.show()

if __name__ =="__main__":
    data = download_data(sticker)
    show_data(data)
    returns = calculate_returns(data)
    plot_daily_returns(returns)
    show_statistics(returns)
    weights = initialize_weights()
    initialize_weights()
    calculate_portfolio_return(returns, weights)
    calculate_portfolio_variance(returns, weights)
    generate_portfolios(initialize_weights(), returns)
    plot_portfolios(generate_portfolios(initialize_weights(), returns)[0], generate_portfolios(initialize_weights(), returns)[1])
    optimize_portfolio(weights, returns)
    print_optimal_portfolio(optimum, returns)
    show_optimal_portfolio(optimum, returns, preturns, pvariances)

