def timer(fn):
    import time
    def inner(*args, **kwargs):
        start = time.time()
        ret = fn(*args, **kwargs)
        end = time.time()
        print("Time elapsed:", end-start)
        return ret
    return inner

# Iterative approach
@timer
def iter_factorial(n):
    return_value = 1
    for i in range(1,n+1):
        return_value = return_value*i
    return return_value

# Recursive approach
@timer
def recur_factorial(n):
    return wrapper(n)

def wrapper(n):
    return 1 if n==1 else wrapper(n-1)*n