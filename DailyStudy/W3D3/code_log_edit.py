""" decorator """

import time

def hello():
    print ("hello world")

def new_hello():
    start_time = time.time()
    hello()
    end_time = time.time()
    exec_time = end_time - start_time
    print ("Execute Time: {time}".format(time=exec_time))

print(new_hello())


# 개선

import time

def hello(name):
    print (name + " hello world")

def track_time(func):
    def new_func(name):
        start_time = time.time()
        func(name)
        end_time = time.time()
        exec_time = end_time - start_time
        print ("Execute Time: {time}".format(time=exec_time))
    return new_func

hello = track_time(hello)
print (hello("박병현"))



""" *args *kwargs 예시 """

def get_arguments(a, *args):  # pack
    print "The first argument is ", a
    for arg in args:
      print("This argument come from args: ", arg)

elements = (1, 2, 3)

print (get_arguments(elements))
# The first argument is  (1, 2, 3)
print (get_arguments(*elements))  #튜플을 unpack
# The first argument is  1
# This argument come from args:  2
# This argument come from args:  3



# 개선 *args, *kwargs

import time

def hello(name):
    print(name + " hello world")

def track_time(func):
    def new_func(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print ("Execute Time: {time}".format(time=exec_time))
    return new_func

hello = track_time(hello)
print (hello("박병현"))


# 개선 @

import time

def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print ("Execute Time: {time}".format(time=exec_time))
    return wrapper

@track_time    # hello = track_time(hello)
def hello(name):
    print (name + " hello world")

print (hello("박병현"))


# 함수의 시작을 알려주는 decorator
# ===== 함수를 시작합니다 =====

# 함수의 종료를 알려주는 decorator
# ===== 함수를 종료합니다 =====
import time

def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print ("Execute Time: {time}".format(time=exec_time))
    return wrapper

def start_func(func):
    def wrapper(*args, **kwargs):
        print("==== 함수시작 ====")
        return func(*args, **kwargs)
    return wrapper

def end_func(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("==== 함수종료 ====")
        return result
    return wrapper

@track_time
@end_func
@start_func    # 밑에가 먼저 랩핑됨
def hello(name):
    print(name + " hello world")

print(hello("박병현"))


""" items
items 함수는 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.

"""

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.items())
# [('phone', '0119993323'), ('name', 'pey'), ('birth', '1118')]



""" 히스토그램 """

data = ["fast", "campus", "fast", "campus", "school", "fast", "fast",]

def histogram(elements):

    # histogram 생성
    hist = {}
    for key in elements:
        hist[key] = 0

    # histogram 데이터 삽입
    for key in elements:
        hist[key] += 1

    # 출력
    for key, values in hist.items():
        print ("{key}{space}{histogram}".format(
            key=key,
            space=" "*(10-len(key)),
            histogram="="*values
        ))

    # 출력 개선 list comprehension

    print ("\n".join([
        "{key}{space}{histogram}".format(
            key=key,
            space=" "*(10-len(key)),
            histogram="="*values
        )
        for key, values
        in hist.items()
    ]))

    # 출력 개선 lambda comprehension

    print ("\n".join(
        list(map(
            lambda key: "{key}{space}{histogram}".format(
                key=key,
                space=" "*(10-len(key)),
                histogram="="*hist[key]
            ),
            hist,
        ))
    ))

print (histogram(data))


""" # sort """

data = [3, 2, 1, 4, 5]
print (sorted(data))
# ['campus', 'campus', 'fast', 'fast', 'fast', 'fast', 'school']

data = [("python", 30), ("ruby", 20), ("javascript", 10)]
print (sorted(data, key=lambda x: x[1]))
print (sorted(data, key=lambda x: x[1])[::-1])    # 역순
# [('javascript', 10), ('ruby', 20), ('python', 30)]
# [('python', 30), ('ruby', 20), ('javascript', 10)]



""" 재귀함수 팩토리얼 """

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

print (factorial(4))


"""
# 피보나치 수열
#0 1 1 2 3 5 8 13 21
# 재귀함수

"""

def fibo(n):
    prev, cur = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        prev, cur = cur, prev + cur
    return cur

for i in range(1000):
    print (fibo(i))


# 개선 재귀함수 + one line if else

def fibo(n):
    return n if n < 2 else fibo(n-1) + fibo(n-2)   # 단점 : 케싱이 없음, 느림

for i in range(10):
    print (fibo(i))


"""
# 결과값을 저장해두는 방법 (memoization)
# 동적 계획법 (기억하며 풀기) (dynamic programming)
# 작은 단위로 나눠서 풀기
# memoization 이 방법 중 하나

"""

# cache 에 딕셔너리로 result 값을 삽입

__cache = {}
def fibo(n):
    if n in __cache:
        return __cache[n]
    else:
        result = n if n < 2 else fibo(n-1) + fibo(n-2)
        __cache[n] = result
        return result

for i in range(1000):
    print (fibo(i))


# 개선 decorator

def memorize(func):
    __cache = {}
    def wrapper(*args):
        if args in __cache:
            return __cache[args]
        else:
            __cache[args] = func(*args)
            return __cache[args]
    return wrapper

@memorize
def fibo(n):
    return n if n < 2 else fibo(n-1) + fibo(n-2)


for i in range(10):
    print (fibo(i))



"""
Class
1. 지금까지는.... 절차 지향적인 프로그래밍을 한것임
2. 이제부터는 객체 지향 프로그래밍 (oop)
상태와 행동이 나뉨
객체 간의 상호작용으로 프로그램이 돌아간다
-----------------------------------------------
3. 함수형 프로그래밍  sicp 책을 추천 1년정도 스터디 해야할 것임
프로그래밍의 패러다임을 바꿔줌

Class, Object, Instance

사람 Class
=> 사람a, 사람b, 사람c, 사람d....

사람a 는 객체(object)다.
사람a 는 사람 Class의 인스턴스(instance)다.

"""


class Person():
    name = "박병현"
    age = 30

    # 함수의 첫번째 인자로는 무조건 객체 자기 자신이 들어간다. self
    def hello(self):
        print(("안녕하세요, {age} 살 {name} 입니다.".format(
            age=self.age,
            name=self.name,
        )))

a = Person()    # 객체 생성
print a.name
print a.age
print a.hello()
# 박병현
# 30
# 안녕하세요, 30 살 박병현 입니다.


# 개선

class Person():

    def __init__(self, name, age):    # __ 파이썬에서 미리 구현된 mathod
        print ("사람이 생성되었습니다.")
        self.name = name
        self.age = age

    def __add__(self, partner):    # __add__ 도 파이썬 최상위 object class에 구현됨
        print("{my_name} 는 {partner_name}와 적극적으로 만난다.".format(
            my_name=self.name,
            partner_name=partner.name,
        ))

    def __str__(self):    # 객체명만 출력할때
        return self.name

    # 함수의 첫번째 인자로는 무조건 객체 자기 자신이 들어간다. self
    def hello(self):
        print(("안녕하세요, {age} 살 {name} 입니다.".format(
            age=self.age,
            name=self.name,
        )))

    def meet(self, another):
        print("{my_name}이 {another_name}을 만났다.".format(
                my_name=self.name,
                another_name=another.name,
        ))

a = Person("박병현", 30)
b = Person("정채연", 20)


print (a + b)
print a
print a.meet(b)


"""  삼각형 """


class Triangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height / 2

    def is_bigger_than(self, another):
        return self.get_area() > another.get_area()

a = Triangle(13,15)
b = Triangle(15,17)


print a.get_area()
print a.is_bigger_than(b)


"""
# 라이브러리 예시

import pandas as pd

df = pd.read_csv("../students.csv")

df



# 책추천

# 파이썬
# 1. 깐깐하게 배우는 파이썬
# 2. 실전 파이썬 프로그래밍

# 장고
# 1. 공식문서

"""
