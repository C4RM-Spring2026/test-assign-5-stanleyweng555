import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    coupon = face * couponRate / ppy
    t = np.arange(1, n + 1)
    pv = (1 + r) ** (-t)
    price = np.sum(coupon * pv) + face * pv[-1]
    return(price)
