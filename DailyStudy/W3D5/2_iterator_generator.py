
# coding: utf-8

"""
# Iterator
# Generator
# iterable

# List :: element
# Dict :: key
# Tuple :: element
# Set :: element
# String :: char(str)

"""

animals = ["dog", "cat", "monkey"]

# List.__iter__() => list_iterator
animals_iterator = animals.__iter__()

# iterator
animals_iterator.__next__()


# animals_iterator = animals.__iter__()
animals_iterator = iter(animals)


# animals_iterator.__next__()
next(animals_iterator)



"""
# elements => elements_iterator => next
# iterable => __iter__ ( iter(____) ) => iterator 객체가 return 되기를 expected
# iterator => __next__ ( next(iterator) ) => element ... raise StopIteration() expected


# range 구현 (iterable 과 iterator가 같이 있어서 생기는 이슈)
# 1회성으로 데이터가 휘발됨 (iterable 재생성을 해야함)


"""


class myrange:

    def __init__(self, n):
        self.i, self.n = 0, n

    def __iter__(self):     # iterable
        return self

    def __next__(self):     # iterator
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()      # 오류를 명시적으로 raise!

myr = myrange(10)


# 한번만 출력 가능
for i in myr:
    print(i)


list(myr)     # 두번째 호출시 리스트가 소멸됨 => myr 은 일회용이됨


class myrange:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return myrange_iterator(self.n) # iterator 생성


class myrange_iterator:

    def __init__(self, n):
        self.i, self.n = 0, n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()  # 해당 오류를 발생시킴

myr = myrange(10)


# iterable 의 분리로 호출할때마다 iterable을 생성함
for i in myr:
    print(i)


list(myr)   # 소멸되지 않음


"""
# Generator
# Iterable => __iter__() iterator expected
# Iterator => __next__() element... StopIteration()
# Generator => Iterator

#Iterable? => generator 결과가 나온다.
#=> generator 는 Iterator 이고,
#iter(generator) 의 결과가 generator 니까
#iterable 하다.

"""


class myrange:   # iterable

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        def myrange_iterator(n):
            i = 0
            while i < n:
                yield i                    # return => "yield"
                i += 1

        return myrange_iterator(self.n)    # generator object


myr = myrange(5)

# 계속 소멸 안됨
for i in myr:
    print(i)

list(myr)


iter(myr)
# <generator object myrange.__iter__.<locals>.myrange_iterator at 0x7fbc0442fdb0>


"""
이러한 특별한 리턴 방식은 다음과 같은 경우에 유용하게 사용된다.

(1) 만약 데이타의 양이 커서 모든 데이타를 한꺼번에 리턴하는 것하는 것 보다
조금씩 리턴하는 것이 더 효율적일 경우.
예를 들어, 어떤 검색에서 1만 개의 자료가 존재하는데,
UI에서 10개씩만 On Demand로 표시해 주는게 좋을 수 있다.
즉, 사용자가 20개를 원할지, 1000개를 원할지 모르기 때문에,
일종의 Lazy Operation을 수행하는 것이 나을 수 있다.

(2) 어떤 메서드가 무제한의 데이타를 리턴할 경우.
예를 들어, 랜덤 숫자를 무제한 계속 리턴하는 함수는 결국 전체 리스트를 리턴할 수
없기 때문에 yield 를 사용해서 구현하게 된다.

(3) 모든 데이타를 미리 계산하면 속도가 느려서 그때 그때
On Demand로 처리하는 것이 좋은 경우. 예를 들어 소수(Prime Number)를
계속 리턴하는 함수의 경우, 소수 전체를 구하면 (물론 무제한의 데이타를 리턴하는
경우이기도 하지만) 시간상 많은 계산 시간이 소요되므로 다음 소수만 리턴하는 함수를
만들어 소요 시간을 분산하는 Lazy Calcuation을 구현할 수 있다.

"""

import time

def very_hard_func(username):
    print("very hard fund")
    time.sleep(2)
    return username + "@gmail.com"


names = ["dobestan", "dobestan2", "dobestan3", "dobestan4", "dobestan5"]


# 일반 함수는 마지막 한 번에 값이 출력됨
[
    very_hard_func(name)
    for name
    in names
]

# very hard fund
# very hard fund
# very hard fund
# very hard fund
# very hard fund
# Out[192]:
# ['dobestan@gmail.com',
#  'dobestan2@gmail.com',
#  'dobestan3@gmail.com',
#  'dobestan4@gmail.com',
#  'dobestan5@gmail.com']



"""  Generator Comprehention  """


gen = (
    very_hard_func(name)
    for name
    in names
)

next(gen)
# very hard fund
# 'dobestan@gmail.com'


# 하나씩 반환함
for i in gen:
    print (i)

# very hard fund
# dobestan2@gmail.com
# very hard fund
# dobestan3@gmail.com
# very hard fund
# dobestan4@gmail.com
# very hard fund
# dobestan5@gmail.com


"""
# 참고자료 : http://haerakai.tistory.com/34

# 공간 = iter(리스트) : iter() 함수를 이용하여 이터레이터를 생성합니다.
# Iterator : 명시된 공간 "b"가 이터레이터입니다.
# Itertion : 이터레이터 b로부터 순차적으로 요소를 가져오는 행위를 말합니다.
# Iterable : 이터레이션이 가능하다는 의미입니다.
# 리스트 != 이터레이터 : 리스트는 이터레이터가 아닙니다. 하지만 이터러블하고 이터레이션이 가능합니다.
# Generator 와 for 문 : 생성기는 일반적으로 for문ㅇ과 짝을 이루어 사용합니다.
# yield : 함수 내에 yield가 포함되면 해당 함수는 생성기라고 부릅니다.
# 생성기 진행의 흐름 : 생성기는 yield를 이용해 값을 반환해도 종료되지 않고 상태를 유지힙니다.

"""

# 생성기 예시
def generator(n):
    while n < 6:
        yield n
        n += 1

for i in generator(0):
    print (i)


# 생성기 루프 확인
def generator(n):
    print ("Generator Start") # 1
    while n < 6:
        print ("Genetator : I give control to the Main") # 2 10 18
        yield n # 3 11 19
        print ("Generator : I received a control.") # 7 15
        n += 1 # 8 16
        print ("Generator : n += 1") # 9 17
    print ("Generator End")

for i in generator(0): # 0
    print ("Main : I received a control.") # 4 12 20
    print (i) # 5 13 ...
    print ("Main : I give control to the Generator") # 6 14


# Generator Start
# Genetator : I give control to the Main
# Main : I received a control.
# 0
# Main : I give control to the Generator
# Generator : I received a control.
# Generator : n += 1
# Genetator : I give control to the Main
# Main : I received a control.
# 1
# Main : I give control to the Generator
# Generator : I received a control.
# Generator : n += 1
# Genetator : I give control to the Main
# Main : I received a control.
# 2
# Main : I give control to the Generator
# Generator : I received a control.
# Generator : n += 1
# Genetator : I give control to the Main
# Main : I received a control.
# 3
# Main : I give control to the Generator
# Generator : I received a control.
# Generator : n += 1
# Genetator : I give control to the Main
# Main : I received a control.
# 4
# Main : I give control to the Generator
# Generator : I received a control.
# Generator : n += 1
# Genetator : I give control to the Main
# Main : I received a control.
# 5
# Main : I give control to the Generator
# Generator : I received a control.
# Generator : n += 1
# Generator End
