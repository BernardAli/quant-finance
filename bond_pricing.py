from math import exp


def zero_bond_price(par_value, market_rate, n):
    return par_value*(1+market_rate)**-n


def coupon_bond_price(par_value, coupon, market_rate, n):
    c = par_value*coupon
    return c/market_rate*(1-(1+market_rate)**-n)+par_value*(1+market_rate)**-n


if __name__ == "__main__":
    par_value = int(input('Enter par value here'))  # par value
    coupon = float(input('Enter coupon rate here'))    # coupon rate
    n = int(input('Enter no. of years here'))   # years
    market_rate = float(input('Enter market rate here'))   #market rate

print(f"Zero Coupon Price: {round(zero_bond_price(par_value, market_rate, n), 4)}")
print(f"Coupon Bond Price: {round(coupon_bond_price(par_value, coupon, market_rate, n), 4)}")

