'''
Author: Hongxiang Qi
Date: 01/07/2021
Description:
Write a recursive function called someRecursive which accepts an array and a callback.
The funciton returns true if a single value in the array returns true when passed to the callback.
Otherwise it returns false.

Example:
    someRecursive([1,2,3,4], isOdd) # true
    someRecursive([4,6,8,9], isOdd) # true
    someRecursive([4.6.8], isOdd) # false
'''

'''
Apporach:
    1. Recursive case - the flow
        someRecursive(arr, cb) = someRecursive(arr[1:], cb(arr[0]))


    2. Base condition - the stopping criterion
        isOdd(num) = true return true
        len(arr) <=0 return false
        
    3. Unintentional case - the constraint
        arr = ["a"] - error - TypeError: not all arguments converted during string formatting
'''

def isOdd(num):
    assert num == int(num), 'the num must be an integer'
    if num%2==0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    assert all(isinstance(x, int) for x in arr), 'the array must contain integer only'
    if cb == True:
        return True
    elif len(arr) <= 0:
        return False
    else:
        return someRecursive(arr[1:], isOdd(arr[0]))

array = [1,3,4]

print(someRecursive(array,isOdd(array[0])))