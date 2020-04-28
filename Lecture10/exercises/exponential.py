import time


def eff_exp(a, b):
    # return a^b
    if b==0:
        return 1
    if b==1:
        return a
    else:
        # previously - f(
        # a,b/2)*f(a,b-b/2)
        if b%2==0:
            out = eff_exp(a, b/2)
            return out*out
        else:
            out = eff_exp(a, int(b/2))
            return out*out*a

def norm_exp(a, b):
    # return a^b
    if b==0:
        return 1
    if b==1:
        return a
    else:
        return norm_exp(a,int(b/2))*norm_exp(a,b-int(b/2))

while True:
    a, b = int(input()), int(input())
    start_time = time.time()
    print(eff_exp(a,b))
    print("--- %s seconds for eff_exp ---" % (time.time() - start_time))

    start_time = time.time()
    print(norm_exp(a,b))
    print("--- %s seconds for norm_exp ---" % (time.time() - start_time))