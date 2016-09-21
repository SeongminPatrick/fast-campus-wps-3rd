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

# 개선

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

# 개선

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

# 개선

def get_awesome_list3(n, *args):
    return [
        "".join([
                arg[1] if (i+1) % arg[0] == 0 else ""
                for arg in args])
            for i
            in range(n)
        ]

# print get_awesome_list3(10, (3, "fast"), (5, "campus"))


""" map """
def double(n):
    return n*2

list(map(
    double,
    range(10)
))

# 개선

list(map(
    lambda x: x*2,
    range(10)
))

# ----------------------------------

def return_fast(n):
    element = ""
    element += "fast" if (n + 1) % 3 == 0 else ""
    return element

list(map(
    return_fast,
    range(10)
))

# 개선

list(map(
    lambda x: "fast" if (x + 1) % 3 == 0 else "",
    range(10)
))


""" List comprehension """
# MAP
# FILTER
# REDUCE

[i*2 for i in range(10)]

# ----------------------------------

[
    "fast" if (i+1) % 3 == 0 else ""  # 함수부분
    for i # 인자
    in range(10) # 연속범위
]


""" filter """

def get_positive(elements):
    result = []
    for elemnet in elements:
        if element > 0:
            result.append(element)
    return result

# 개선

list(filter(
    lambda x: x > 0,  # 조건
    [-1, -2, -4, 5, 3, 2]  # 대상
))

# 개선

[
    i
    for i # 함수
    in [-1, -2, -4, 5, 3, 2]  # 범위
    if i > 0  # 조건
]

# range(1, 11) 제곱 [1, 4, ..... 100] 중에서 50보다 큰 수만 리스트

def over50(n):
    result = []
    for i in range(1, n):
        if i**2 > 50:
            result.append(i**2)
    return result

# lambda로

list(filter(
        lambda x: x > 50,
        list(map(lambda i: i**2, range(1,11)))
))

# list comprehension 으로

[
    i**2
    for i
    in range(1,11)
    if i**2 > 50
]

from functools import reduce

def add(a, b):
    return a + b

reduce(add, [1, 2, 3, 4, 5])

# 개선

reduce(
    lambda x, y: x + y, # 인수 2개 함수
    range(1, 11) # 범위
)

# 인자를 두개 만 받는다 항상
# 앞에서부터 두 개씩 연산해 나간다
# 그래서 줄여간다는 reduce

# ------------------------------

reduce(
    lambda x, y: x if x > y else y,
    [1, 3, 4, 5, 6, -1]
)


""" rent 평균 구하기 """

data = [
    {"rent": 50, "deposit": 1000},
    {"rent": 55, "deposit": 2000},
    {"rent": 60, "deposit": 4000},
]

sum_rent = 0
sum_diposit = 0

for i in data:
    sum_rent += i["rent"]
    av_rent = sum_rent / len(data)

# 람다로

reduce(
    lambda x, y: {"rent" : x["rent"] + y["rent"], "deposit": x["deposit"] + y["deposit"]},
    data
    )["rent"]/len(data)

# 개선

reduce(
    lambda x, y: x + y,
    [
        i["rent"]
        for i
        in data
    ]
)/len(data)


"""
args, kargs (pack unpack)
*가 인자를 하나로 묶고 나눈다

"""

def hello(*args):
    return (args)

data = ["monkey", "cat", "dog"]

hello(data)
hello(*data)
# (['monkey', 'cat', 'dog'],)
# ('monkey', 'cat', 'dog')

def hello2(*args, **kwargs):
    return args, kwargs

hello2(2,3,4, name="dobest", email="dobest@gmail.com")
# ((2, 3, 4), {'name': 'dobest', 'email': 'dobest@gmail.com'})
# 키워드가 있는 애와 없는애를 나눠서 묶는다


""" fast campus return 응용 """

def get_awesome_list5(n, *args):
    result = []
    for i in range(n):
        element = ""
        for arg in args:
            div, text = arg
            element += text if (i + 1) % div == 0 else ""
        result.append(element)
    return result

get_awesome_list5(10, (3, "fast"), (5, "campus"), (7, "school"))

# 리스트로

def get_awesome_list6(n, *args):
    return [
        "".join([
            arg[1] if (i + 1) % arg[0] == 0 else ""
            for arg
            in args
        ])
        for i
        in range(n)
    ]

get_awesome_list6(10, (3, "fast"), (5, "campus"), (7, "school"))

# 람다로 (숙제)

def get_awesome_list(n, *args):
    return list(map(
        lambda i: "".join(list(map(
            lambda arg: arg[1] if (i + 1) % arg[0] == 0 else "",
            args
        ))),
        range(n)
    ))

get_awesome_list(10, (3, "fast"), (5, "campus"), (7, "school"))
