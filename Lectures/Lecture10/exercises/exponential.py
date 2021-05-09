import time


def eff_exp(a, b):
    '''
    a^b -> a^(b/2)*a^(b/2) otherwise a^(b/2)*a^(b/2)*a
    '''
    if b==0:
        return 1
    else:
        half = eff_exp(a, int(b/2))
        return half*half*a if b%2==1 else half*half

def norm_exp(a, b):
    # base case
    if b==0:
        return 1
    # recursion step
    return a*norm_exp(a, b-1)

while True:
    a, b = int(input()), int(input())
    start_time = time.time()
    print(eff_exp(a,b))
    print("--- %s seconds for eff_exp ---" % (time.time() - start_time))

    start_time = time.time()
    print(norm_exp(a,b))
    print("--- %s seconds for norm_exp ---" % (time.time() - start_time))