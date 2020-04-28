'''
Given a string as input print "Palindrome" if it's a palindrome and "Not palindrome" if it's not
Examples of palindrome - abcdcba
'''

def is_palindrome(inp_string):
    # base case
    if len(inp_string)<=1:
        return True
    else:
        # recursion step
        if inp_string[0] == inp_string[-1]:
            return is_palindrome(inp_string[1:-1])
        else:
            return False

while True:
    print(is_palindrome(input()))