'''
Author: Hongxiang Qi
Date: 30/06/2021
Description:
Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome
(reads same forward and backward).
Otherwise it returns false

Example:
    isPalindrome('awesome') # false
    isPalindrome('foobar') # false
    isPalindrome('tacocat') # true
    isPalindrome('amanaplanacanalpanama') # true
    isPalindrome('amanaplanacanalpandemonium') # false

'''

'''
Apporach:
    1. Recursive case - the flow
        isPalindrome(s) =  isPalindrome(s[1:len(s)-1])


    2. Base condition - the stopping criterion
        len(s) = 0 return True
        s[0] != s[len(s)-1] return false

    3. Unintentional case - the constraint
        s = None - error - TypeError: object of type 'NoneType' has no len()
        s = 123 - error - TypeError: object of type 'int' has no len()
'''

def isPalindrome(s):
    assert s == str(s), 'input must be a string'
    if len(s) == 0:
        return True
    elif s[0] != s[len(s)-1]:
        return False
    else:
        return isPalindrome(s[1:len(s)-1])

string = "tacocat"

print(isPalindrome(string))