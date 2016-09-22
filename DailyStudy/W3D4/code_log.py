# -*- conding: utf-8 -*-

"""
========================================================================
class

"""

class Animal():

    # 기본제공 함수, 외부에서 호출 못함 "__"
    def __init__(self, anitype, weight):
        self.anitype = anitype
        self.weight = weight

    def eat(self):
        return("먹이를 먹습니다.")

    def is_heavir_than(self, another):
        return self.weight > another.weight

# 인스턴스 생성
d4 = Animal("dog", 4)
d5 = Animal("dog", 5)
c6 = Animal("cat", 6)
c3 = Animal("cat", 3)

print(d4.anitype)
print(d4.is_heavir_than(c3))
print(d4.eat())


# 개선

class Animal():

    def __init__(self, type, weight):
        self.type = type
        self.weight = weight

    # Polymorphism - Parametic Polymorhism ( Overloading ) - 더 많이 argument 로드
    def eat(self, *args):
        if not args:
            print ("먹이를 먹습니다.")
        for arg in args:
            print("\n".join([
                "{feed} 을/를 먹습니다.".format(
                    feed=arg
                )
            ]))

    def swim(self):
        return ("해엄을 친다." if self.type == "fish" else "물에 빠진다.")


d4 = Animal("dog", 4)
d5 = Animal("dog", 5)
c6 = Animal("cat", 6)
c3 = Animal("cat", 3)
f10 = Animal("fish", 10)


print(d4.eat("소시지", "감자", "햄"))
print(d5.eat())
print(f10.swim())
print(d4.swim())


"""
========================================================================
# 상속 ( Inheritance )
# 삼각형, 사각형

# width, height
# area => w * h / 2
# area => w * h

높이 너비 값받고
크기비교하고
다른 클래스면 오류처리하고
Triangle
Rectangle
Shape
========================================================================

"""

class Shape():

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def is_bigger_than(self, another):
        # 다른 class Instance와 비교 막기 - sub-Type Polymorphism
        if not isinstance(another, Shape):
            print("오류")
        else:
            return self.area > another.area

# Shape class 상속 받음
class Triangle(Shape):
    def area(self):
        return self.height * self.height / 2

class Rectangle(Shape):
    def area(self):
        return self.height * self.height


tri = Triangle(10, 20)
rec = Rectangle(10, 20)

print(tri.area())
print(tri.is_bigger_than(rec))


# sub-Type Polymorphism 테스트
class Room:

    def __init__(self, real_area):
        self.real_area = real_area

    def area(self):
        return self.real_area

room = Room(200)

print(tri.is_bigger_than(room))


""" Instance class 확인법
========================================================================
# 1. 정확한 비교 => type
# 2. 상속? => isinstance(객체, 클래스)
# 3. 상속? => issubclass(클래스, 클래스)
========================================================================

"""

# 정확한 클래스 확인
print(type(tri) is Triangle)
# 서브 클레스 확인
print(issubclass(Triangle, Shape))
# 클래스 확인 (단, 클래스가 아니어도 타입 확인이 가능함)
print(isinstance("박병현", str))    # True
print(isinstance("박병현", int))    # False
print(isinstance("박병현",(str, int)))    # True


""" Overriding """

class Animal():

    def __init__(self, weight):
        self.weight = weight

    def is_bigger_than(self, animal):
        return self.weight > animal.weight

    def eat(self):
        print("먹이를 먹는다.")


class Dog(Animal):

    def eat(self):   # * Overriding ( 메쏘드 오버라이딩 )
        print("침을 흘리면서 먹는다.")


d3 = Dog(3)
d4 = Dog(4)

print(d3.eat())    # 침을 흘리면서 먹는다. (하위 클래스의 eat을 출력)


"""
========================================================================

# 관계형 데이터베이스 ===> SQL ( Structured Query Lang ) ====> 데이터
# ORM ( Object Relational Mapping ) ::
                        Ruby on Rails (Django ORM <<< Python::SQL Alchemy)
# CRUD ( Create Retrieve Update Destroy )

# 클래스 => 객체 ( row 1개 => 객체 1개 ; column => attribute ; + Behavior )
                                                    => MVC Framework :: Model

# SQL... => 클래스, 객체 ( SQL )
# user.send_sms(content) => User의 핸드폰번호를 바탕으로 문자 메시지를 보내는 "기능"

# 1.4 => 1.5 CBV

# TemplateView Class .... TemplateView.as_function()
# Class Based View ( 55 )    <= 중요
# O2O => 일반적인 서비스. ... 3-4 Model,

# FBV, CBV
========================================================================


Instance Mathod
Class Mathod
Static Method

# 되도록 instance method 는 instance 만 불러오고
# class method 는 class 만 불러오는게 좋다


"""

class Awesome():

    def __init__(self, name):
        self.__name = name

    @property    # .ㅜname 만 입력해도 함수로 처리된다
    def name(self):
        print("Getter Called")
        return self.__name    # __로 attribute 를 내부에서만 사용한다

    """ Instance Method """
    def my_instance_method(self):
        return self

    """ Class Method """
    @classmethod
    def my_class_method(cls):
        return cls     # class 를 받고 class를 반환한다

    """ Static Method """
    # ( Class/Instance 와 무관하게 ) , argument를 받지 않는다
    # Behavior 만 있고 Status 는 없다
    @staticmethod
    def my_static_method():
        return "static"

# property
awesome = Awesome("name")
awesome.name = "dobestan"
print(awesome.name)

# staticmethod - class instance 모두 호출 할 수 있음
print(awesome.my_static_method())
print(Awesome.my_static_method())


# property 예시 추가

class User:

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @property
    def full_name(self):
        return self.last_name + self.first_name

user = User("안", "수찬")
print(user.full_name)



"""
========================================================================

# login_required   유저가 로그인 되었는지
# is_admin         유저가 관리자인지


# User Class :: username, is_admin


# Request    :: user instance ( user O => 로그인 O ; user X => 로그인 X ), url(string)
#    request = Request()
#    request.user
#
# Response   :: body(string)
========================================================================

User
    네임 어드민 권한 입력
Request
     url, user 여부 입력
Response
    body text 출력
"""

class User():

    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


class Request():

    def __init__(self, url, user=None):
        self.url = url
        self.user = user

class Response():

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return "Response :: {body}".format(body=self.body)

# user 생성
pbhfaith = User("박병현")
admin = User("관리자", is_admin=True)


# mypage
def mypage(request):
    if request.user:  # request 객체에 user 값이 있으면 True
        response = Response("정상적으로 MyPage 접속합니다.")
    else:
        response = Response("로그인이 필요합니다.")
    return response

#request 객체
request = Request("/mypage/", pbhfaith)

# mypage로 request
print(mypage(request))



""" decorator로 개선 """


class User():

    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


class Request():

    def __init__(self, url, user=None):
        self.url = url
        self.user = user


class Response():

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return "Response :: {body}".format(body=self.body)


# user 생성
pbhfaith = User("박병현")
admin = User("관리자", is_admin=True)


def login_required(func):
    def wrapper(request, *args):
        if request.user:
            response = func(request, *args)
        else:
            response = Response("로그인이 필요합니다.")
        return response
    return wrapper

@login_required
def mypage(request):
    return Response("정상적으로 MyPage 접속합니다.")

request = Request("/mypage/", pbhfaith)
print(mypage(request))




""" is admin 작성 """



class User():

    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


class Request():

    def __init__(self, url, user=None):
        self.url = url
        self.user = user


class Response():

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return "Response :: {body}".format(body=self.body)


# user 생성
pbhfaith = User("박병현")
admin = User("관리자", is_admin=True)


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user:
            response = func(request, *args, **kwargs)
        else:
            response = Response("로그인이 필요합니다.")
        return response
    return wrapper

def is_admin(func):
    def wrapper(request, *args, **kwargs):
        if request.user:
            response = func(request, *args, **kwargs)
        else:
            response = Response("관리자 권한이 필요합니다.")
        return response
    return wrapper

@is_admin
@login_required
def admin(request):
    return Response("성공적으로 Admin 에 접속했습니다.")


request = Request("/admin/")
print(admin(request))


request = Request("/admin/",pbhfaith)
print(admin(request))


"""
========================================================================
크롤링
# https://github.com/kennethreitz/requests/tree/master/requests
# request

# Request :: HTTP Method(GET, POST, PATCH, PUT, DELETE), URL, Headers

"""
import requests
response = requests.get("http://www.naver.com/")
print (response.status_code)  # 200 OK ( 404 NOT FOUND, 301 REDIRECT )
print (response.text)

"권혁수" in response.text

element.select_one("a").attrs["title"]    # a tag select ..... title 값 찾기

# 네이버 실시간 검색어 크롤링 리스트에 삽입
[
    element.select_one("a").attrs["title"]
    for element
    in elements[:-1]  # 네이버가 마지막 하나를 더 반화해서 빼버림
]

# 1. 정적인 사이트 (server rendering) = 네이버, 일반 홈페이지
# 2. 동적인 사이트 (Client Rendering :: API, Ajax ) - 직방, 다방, 요기요....
# 3. 한국형 사이트 (Javascript) - 사내 인트라넷, 아주 옛날 공공기관 데이터 뽑아주는곳?
# 4. 한국형 사이트 (iFrame) - 네이버 카페, 옛날 사이트
# =====================================

# 보안이 걸려있는 사이트
# 사이트 => 이걸 어떻게 접근해야 할까?
