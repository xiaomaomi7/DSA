'''
Author: Hongxiang Qi
Date: 22/06/2021
Description:
Write a recursive function called fib which accepts a number and returns the nth number in the
Fibonacci sequence. Recall that the Fibonacci sequence is the sequence of whole numbers 0,1,1,2,3,5,8,...
which starts with 0 and 1, and where every number thereafter is equal to the sum of the previous two numbers.

Example:
    fib(4) # 3
    fib(10) # 55
    fib(28) # 317811
    fib(35) # 9227465
'''

'''
Apporach:
    1. Recursive case - the flow
        fib(n) = fib(n - 1) + fib(n - 2)


    2. Base condition - the stopping criterion
        n = 0, return 0
        n = 1, return 1

    3. Unintentional case - the constraint
        fib(1.1) - error - RecursionError: maximum recursion depth exceeded in comparison
        fib(-1) - error - RecursionError: maximum recursion depth exceeded in comparison
'''

def fib(n):

    assert n == int(n) and n >= 0, 'The input n must be an integer and positive.'
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(4))