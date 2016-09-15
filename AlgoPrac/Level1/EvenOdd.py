# -*- coding: utf-8 -*-
"""
evenOrOdd 메소드는 int형 num을 매개변수로 받습니다.
num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하도록 evenOrOdd에 코드를 작성해 보세요.
num은 0이상의 정수이며, num이 음수인 경우는 없습니다.
"""

def evenOrOdd(num):
    if num % 2 == 0:
        s = "Even"
    else :
        s = "Odd"
    return s

print evenOrOdd(3)
print evenOrOdd(4)
