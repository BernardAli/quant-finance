from math import exp

def perpetuity(c, r):
    pv = c/r
    return pv

def growth_perpetuity(c, r, g):
    pv = c/(r-g)
    return pv

if __name__ == "__main__":
    c = int(input('Enter amount of each continuous payment here'))
    r = float(input('Enter rate here'))
    g = float(input('Enter growth rate here'))


print("Perpetuity", perpetuity(c, r))
print("Perpetuity with growth", growth_perpetuity(c, r, g))