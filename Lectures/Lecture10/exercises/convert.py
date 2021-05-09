

def to_base2(num):
    pass

def to_base10(num):
    # base case
    if num/10==0:
        return num
    # recursive step
    '''
    101 = 5
    10, 1 = to_base10(10)*2+1
    '''
    # 101011101  1
    # 2*to_base10(101011101)+1
    return 2*to_base10(int(num/10))+num%10