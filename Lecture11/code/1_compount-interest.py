def raiseToPower(n,k):
    if (k == 1):
        return n
    else:
        return n*raiseToPower(n,k-1)

def compountInterest(p, r, t):
    return p * raiseToPower((1 + (r/100)), t)

print(compountInterest(10000, 8, 5))