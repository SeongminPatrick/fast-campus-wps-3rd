# -*- coding: utf-8 -*-
"""
sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.
예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.
sum_digit함수를 완성해보세요.
"""

def sum_digit(number):
    # number = str(number)
    # numbers = []
    # result = 0
    # for i in number:
    #     result += int(i)
    # return result

    if number < 10:
        return number
    else:
        return number % 10 + sum_digit(number / 10)

print("결과 : {}".format(sum_digit(1233424234223343)));
