# -*- coding: utf-8 -*-
"""
no_continuous함수는 스트링 s를 매개변수로 입력받습니다.

s의 글자들의 순서를 유지하면서, 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.
예를들어 다음과 같이 동작하면 됩니다.

s가 '133303'이라면 ['1', '3', '0', '3']를 리턴
s가 '47330'이라면 [4, 7, 3, 0]을 리턴
"""

# def no_continuous(s):
#     result = []
#     for i in range(len(s)):
#         if i == 0 or s[i] != s[i-1]:
#             result.append(s[i])
#     return result

def no_continuous(s):
    return [ result for i, result in enumerate(s) if i == 0 or s[i-1] != s[i] ]

print( no_continuous( "13330311" ))
