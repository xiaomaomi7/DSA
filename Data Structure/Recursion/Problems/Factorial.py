'''
Author: Hongxiang Qi
22/06/2021
Write a function factorial which accepts a number and returns the factorial of that number.
A factorial is the product of an integer and all the inegers below it;
e.g., factorial four(4!) is equal to 24,
because 4 * 3 * 2 * 1 equals 24. factorial zero(0!) is always 1.


Example:
    factorial(1) # 1
    factorial(2) # 2
    factorial(4) # 24
    factorial(7) # 5040
'''

'''
Apporach:
    1. Recursive case - the flow
        n! = n * (n-1)!

    2. Base condition - the stopping criterion
        n = 0 return 1
        n = 1 return 1

    3. Unintentional case - the constraint
        factorial(1.1) - Error - RecursionError: maximum recursion depth exceeded in comparison
        factorial(-1) - Error - RecursionError: maximum recursion depth exceeded in comparison
'''

def factorial(n):
    assert n == int(n) and n >= 0, "The input n must be an integer and positive!"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(1))
