import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    coupon = face * couponRate / ppy
    t = np.arange(1, n + 1)
    pv = (1 + r) ** (-t)
    cf = np.full(n, coupon)
    cf[-1] += face
    pvcf = pv * cf
    price = np.sum(pvcf)
    duration = np.sum(t * pvcf) / price / ppy
    return(duration)
