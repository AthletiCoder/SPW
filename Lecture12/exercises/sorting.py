# fixed range between 1-n
l = [4,7,2,8,3,9]
# best so far is nlog(n) without any extra memory

# input array size m
n = 10
myList = [0 for i in range(n)]

# storage memory [0 0 0 0 0 0 0 0 0]

for element in l:
    myList[element] = 1

for i in range(len(myList)):
    if myList[i]:
        print(i)