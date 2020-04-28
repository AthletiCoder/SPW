



'''
Given a number, n, do the following
* Print "Pling" p number of times, where p is the power of 3 in prime factorization of n
* Print "Plang" q number of times, where q is the power of 5 in prime factorization of n
* Print "Plong" r number of times, where r is the power of 7 in prime factorization of n
* If n is not divisible of any of 3,5,7 then return the number, n, as it is
'''

n = int(input())

sounds = {3:"Pling", 5:"Plang", 7:"Plong"}

output = ""
for num, sound in sounds.items():
    while n%num==0:
        n = n/num
        output = output+sound

if output == "":
    output = str(n)

print(output)
