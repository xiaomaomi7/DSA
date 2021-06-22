'''
Author: Hongxiang Qi
Date: 22/06/2021
Description:
Write a function called productOfArray which takes in an array of numbers

Example:
    productOfArray([1,2,3]) # 6
    productOfArray([1,2,3,10]) # 60
'''

'''
Apporach:
    1. Recursive case - the flow
        product(array) = array(0) * product(array[1:])
        

    2. Base condition - the stopping criterion
        length of array is 1 return array[0]

    3. Unintentional case - the constraint
        productOfArray([]) - error - IndexError: list index out of range
        productOfArray([-1,1]) - Pass
        productOfArray([1.1,1]) - Pass
        productOfArray([-2,1.1,1]) - Pass
'''

def productOfArray(array):
    assert len(array) > 0, 'The array is empty.'
    if len(array) == 1:
        return array[0]
    else:
        return array[0] * productOfArray(array[1:])

print(productOfArray([-2,1.1,1]))


