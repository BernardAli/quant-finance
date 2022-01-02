from math import exp

# present value of annuity
def pv_annuity(pmt, r, n):
    pv = pmt/r * (1 - (1+r)**-n)
    return pv

def annuity_due(pmt, r, n):
    pv = pmt/r * (1 - (1 * (1+r)**-n)) * (1+r)
    return pv

def annuity_growth(pmt, r, n, g):
    pv = (pmt/(r-g))((1+r)**n - (1+g)**n)

# future value
def fv_annuity(pmt, r, n):
    fv = pmt/r * ((1+r)**n-1)
    return fv

def fv_annuity_due(pmt, r, n):
    fv = pmt/r * ((1+r)**n-1) * (1+r)
    return fv


if __name__ == "__main__":
    pmt = int(input('Enter amount of each annuity payment here'))
    r = float(input('Enter rate here'))
    n = float(input('Enter no. of years here'))

print("PV Annuity ", pv_annuity(pmt, r, n))
print("Annuity Due", annuity_due(pmt, r, n))
print("FV Annuity", fv_annuity(pmt, r, n))
print("FV Annuity Due", fv_annuity_due(pmt, r, n))