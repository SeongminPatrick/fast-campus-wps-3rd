# -*- coding: utf-8 -*-

""" algorism_1
n input n개의 짝수 리스트 리턴

"""

def double_number(n):
    result = []
    for i in range(n):
        result.append(i*2)
    return result

# print double_number(100)


""" algorism_2
n input n 보다 작은 짝수 리스트

"""
def double_under(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

# print double_under(100)


""" algorism_3
n 까지의 소수 100
두 개의 함수로 나눠서 해석

"""
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# print is_prime(6)

def main_prime(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

# print main_prime(100)


"""algorism_4
3의 배수는 "fast" 5의 배수는 "campus" 나머지 빈칸 리턴 식으로 리턴
단계별로 접근해보자

"""

def return_fast(n):
    result1 = []
    for i in range(n):
        element = "fast" if (i+1) % 3 == 0 else ""
        result1.append(element)
    return result1

# print return_fast(100)

def return_campus(n):
    result2 = []
    for i in range(n):
        element = "campus" if (i+1) % 5 == 0 else ""
        result2.append(element)
    return result2

# print return_campus(100)

def fastcampus_mix(n):
    result = []
    for i in range(n):
        element = ("fast" if (i + 1) % 3 == 0 else "") + ("campus" if (i + 1) % 5 == 0 else "")
        result.append(element)
    return result

# print fastcampus_mix(10)


""" 개선 """

def get_awesome_list(rule1, rule2):
    result = []
    for i in range(100):
        element = ""
        for rule in [rule1, rule2]:
            div, text = rule
            element += text if (i + 1) % div == 0 else ""
        result.append(element)
    return result

print get_awesome_list((3, "fast"), (5, "campus"))



""" 개선 """

def get_awesome_list2(n, *args):
    result = []
    for i in range(n):
        element = ""
        for arg in args:
            div, text = arg
            element += text if (i + 1) % div == 0 else ""
        result.append(element)
    return result

# print get_awesome_list2(10, (3, "fast"), (5, "campus"))

""" 개선 """

def get_awesome_list3(n, *args):
    return [
        "".join([
                arg[1] if (i+1) % arg[0] == 0 else ""
                for arg in args])
            for i
            in range(n)
        ]

# print get_awesome_list3(10, (3, "fast"), (5, "campus"))
