'''
Author: Hongxiang Qi
Date: 30/06/2021
Description:
Write a recursive fucntion called flatten which accepts an array of arrays
and returns a new array with all values flattened.

Example:
    flatten([1,2,3,[4,5]]) # [1,2,3,4,5]
    flatten([1,[2,[3,4],[[5]]]]) # [1,2,3,4,5]
    flatten([[1],[2],[3]]) # [1,2,3]
    flatten([[[[1],[[[2]]],[[[[[[[3]]]]]]]]]) # [1,2,3]

'''

'''
Apporach:
    1. Recursive case - the flow
        flatten(arr) = arr[:1] + flatten(arr[1:])


    2. Base condition - the stopping criterion
        len(arr) <= 0 return arr
        len(arr[0]) = list return flatten(arr[0]) + flatten(arr[1:])

    3. Unintentional case - the constraint

'''

def flatten(arr):
    if len(arr) <= 0:
        return arr
    elif isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    else:
        return arr[:1] + flatten(arr[1:])

array = [1,2,3]

print(flatten(array))