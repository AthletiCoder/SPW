'''
Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if a one number is a factor of another is to use the modulo operation (%).

The rules of raindrops are that if a given number:

* has 3 as a factor, add 'Pling' to the result.
* has 5 as a factor, add 'Plang' to the result.
* has 7 as a factor, add 'Plong' to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

Examples
--------
* 28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
* 30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
* 34 is not factored by 3, 5, or 7, so the result would be "34".
'''

inp = int(input())

# Begin your code here to achieve results as explained above
res = ""
if not inp%3:
    res+="Pling"
if not inp%5:
    res+="Plang"
if not inp%7:
    res+="Plong"
if not res:
    res=str(inp)

print(res)