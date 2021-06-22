'''
19/06/2021
Write a function called power which accepts a base and exponent.
The function should return the power of the base to the exponent.
This function should mimic the functionality of math.pow()
Do not worry about the Negative bases and exponents.

Example:
    Power(2,0) # 1
    Power(2,2) # 4
'''

'''
Apporach:
    1. Recursive case - the flow
        x**n = x * x**n-1
        
    2. Base condition - the stopping criterion
        n = 0 return 1
        n = 1 return base
        
    3. Unintentional case - the constraint
        power(3.2,2) - pass
        power(2,1.2) - error - maximum recursion depth exceeded in comparison
'''
def power(base, exp):

    assert exp == int(exp), 'The exponent must be an integer'
    assert base >= 0 and exp >= 0, 'The base and the exponent must be positive'

    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base, exp - 1)

print(power(2,10))