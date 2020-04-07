def factorial(x):
    if x < 0:
        raise ValueError('negative number passed')
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)

def combinatorial(n,k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))

print(combinatorial(-2,-1))
