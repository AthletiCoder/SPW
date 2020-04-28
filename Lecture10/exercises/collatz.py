'''
Applies to positive integers and speculates that it is always possible to get "back to 1" if one follows the below steps
* If n is 1 stop
* Otherwise, if n is even, repeat this process on n/2
* Otherwise, if n is odd, repeat this process on 3n+1

Prove the above conjecture by plotting a graph for number of steps taken to reach 1 for first 100 natural numbers
'''

def count(n):
    '''
    returns the number of steps taken for n to reach 1
    '''
    # base case
    if n==1:
        return 1
    # recursive step
    if n%2==0:
        return count(n/2)+1
    else:
        return count(3*n+1)+1

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,1001,1)
y = list(map(count,x))

plt.plot(x,y)
plt.show()