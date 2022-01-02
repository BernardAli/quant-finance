import math


def net_present_value(rate, cashflows):
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate) ** i
    return total

cashflows = [-100, 20,40, 50, 20, 10]
r = 0.05

print(net_present_value(r, cashflows))


def IRR(cashflows,interations=100):
    rate = 1.0
    investment = cashflows[0]
    for i in range(1, interations+1):
        rate *= (1-net_present_value(rate,cashflows)/investment)
    return rate

print(IRR(cashflows))