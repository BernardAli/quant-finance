import math
import pandas as pd
import numpy as np
from scipy import stats


def blackscholes_call(S, E, T, rf, sigma):
    # first we have to calculate d1 and d2 parameters
    d1 = (np.log(S/E) + (rf+sigma*sigma/2.0)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    print(d1)
    print(d2)

    # we need N(x) normal distribution function
    return S*stats.norm.cdf(d1) - E*np.exp(-rf*T)*stats.norm.cdf(d2)

def blackscholes_put(S, E, T, rf, sigma):
    # first we have to calculate d1 and d2 parameters
    d1 = (np.log(S / E) + (rf + sigma * sigma / 2.0) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # we need N(x) normal distribution function
    return -S*stats.norm.cdf(-d1) + E*np.exp(-rf*T)*stats.norm.cdf(-d2)

if __name__ == "__main__":
    S0 = 100        # underlying stock price at t=0
    E = 100         # strike price
    T = 1           # expiry (year)
    rf = 0.05       # risk-free rate
    sigma = 0.2     # volatility of the underlying stock

    print('Call option price according to Black-Scholes model:', blackscholes_call(S0, E, T, rf, sigma))
    print('Put option price according to Black-Scholes model:', blackscholes_put(S0, E, T, rf, sigma))