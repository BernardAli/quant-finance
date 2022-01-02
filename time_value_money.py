from math import exp
# import numpy as np

# Discrete Values
def discrete_future_value(x, r, n):
    return x * (1 + r)**n

def discrete_present_value(x, r, n):
    return x * (1 + r)**-n


# Continous Values
def continuous_future_value(x, r, t):
    return x*exp(r*t)

def continuous_present_value(x, r, t):
    return x*exp(-r*t)


#  With No. of periods
def periods_future_value(x, r, n, p):
    return x * (1 + (r/p)) ** (n*p)

def periods_present_value(x, r, n, p):
    return x * (1 + (r/p)) ** -(n*p)


# Effective Annual Rate
def effective_annual_rate(x, r, n, p):
    return ((1+r/p)**p)-1

'''def apr_conversion(apr1, p1, p2):
    apr2 = (1+(apr1/p1))**(p1/p2) - 1
    return apr2'''

if __name__ == "__main__":
    x = int(input('Enter price here'))
    r = float(input('Enter rate here'))
    n = float(input('Enter no. of years here'))
    p = int(input('This is computed based on the number of occurrences in a year'))  # This is computed based on the number of occurrences in a year
    # p1 = int(input('Number of periods for assets 1'))
    # p2 = int(input('Number of periods for assets 2'))
    # apr1 = float(input('APR for asset 1'))

print('Future Value:')
print('Discrete Future Value: ', discrete_future_value(x, r, n))
print('Continuous Future Value: ', continuous_future_value(x, r, n))
print('Periods Future Value:', periods_future_value(x, r, n, p))

print('\nPresent Value:')
print('Discrete Present Value: ', discrete_present_value(x, r, n))
print('Continuous Present Value: ', continuous_present_value(x, r, n))
print('Periods Present Value:', periods_present_value(x, r, n, p))

print('\nEffective Annual Rate')
print('Effective Annual Rate', effective_annual_rate(x, r, n, p))
# print('Apr Conversion', apr_conversion(apr1, p1, p2))



