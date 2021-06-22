'''
Author: Hongxiang Qi
Date: 22/06/2021
Description:
Write a function called recursiveRange which accepts a number and adds up all the numbers
from 0 to the number passed to the function

Example:
    recursiveRange(6) # 21
    recursiveRange(10) # 55
'''

'''
Apporach:
    1. Recursive case - the flow
        recursiveRange(n) = n + recursiveRange(n-1)


    2. Base condition - the stopping criterion
        n = 0, return 0

    3. Unintentional case - the constraint
        recursiveRange(-1) - error - RecursionError: maximum recursion depth exceeded in comparison
        recursiveRange(1.1) - error - RecursionError: maximum recursion depth exceeded in comparison
'''

def recursiveRange(n):
    assert n == int(n) and n >= 0, 'The input n must be an integer and positive'
    if n == 0:
        return 0
    else:
        return n + recursiveRange(n - 1)

print(recursiveRange(100))