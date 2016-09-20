# -*- coding: utf-8 -*-

def is_palindrome1(string):
    length = len(string)
    for i in range(length):
        left = string[i]
        right = string[length -1 -i]

        if left != right:
            return False
        else:
            return True

""" 개선 """
def is_palindrome2(string):
    return string == string[::-1]


""" 축약 """
is_palindrome3 = lambda x : x == x[::-1]


print is_palindrome3("assa")
