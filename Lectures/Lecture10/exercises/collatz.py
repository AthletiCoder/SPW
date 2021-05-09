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
    if n==1:
        return 0
    if n%2==0:
        return count(n/2)+1
    else:
        return count(3*n+1)+1

import numpy as np

x = np.arange(1,11)
y = []
for i in x:
    y.append(count(i))

y = np.array(y)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()