'''
Author: Hongxiang Qi
Date: 27/06/2021
Description:
Write a recursive function called reverse which accepts a string and
returns a new string in reverse.

Example:
    reverse('python') # 'nohtyp'
    reverse('appmillers') # 'srellimppa'
'''

'''
Apporach:
    1. Recursive case - the flow
        reverse(s) = s[-1] + reverse(s[:len(s)-1])


    2. Base condition - the stopping criterion
        len(s) <= 0 return ""

    3. Unintentional case - the constraint
        s = "" - pass
        s = "Py1thon" - pass
        s = None - error - TypeError: object of type 'NoneType' has no len()
        s = 123 - error - TypeError: object of type 'int' has no len()
'''

def reverse(s):
    assert s == str(s), 'input must be a string'
    if len(s) <=0:
        return ""
    else:
        return s[-1] + reverse(s[:len(s)-1])

string = "Python"

print(reverse(string))