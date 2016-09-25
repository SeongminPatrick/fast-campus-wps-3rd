
"""
# coding: utf-8


# 1. html 파일을 가져오는 단계 ( = scraping, crawling )
# 2. html 파일 내에서 원하는 텍스트만 추출 ( = parsing )

# CSS Selector
# "realrank" 라는 id 를 가진 ul 안에 => 10개의 li 태그
# ul#realrank li

# 네이버 블로그 검색 결과
# ul#elThumbnailResultArea li.sh_blog_top

# tag => text
# id => #
# class => .

# CSS Selector ... class

"""


import requests
from bs4 import BeautifulSoup



# 크롤링할 url을 가져온다
response = requests.get(
    "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=python"
    )
# bs4 라이브러리의 html.parser을 사용한다
bs = BeautifulSoup(response.text, "html.parser")
post_elements = bs.select("ul#elThumbnailResultArea li.sh_blog_top")

len(post_elements)


"""
# 크롤링 디펜스 방법
# 1. IP :: Server IP(AWS EC2), IP 를 변경
# 2. 초당 Request ... 기다림!
# 3. `requests.get` .. HTTP Request Headers(Meta)

# user agent 변경해서 크롤링
# requests,,, => iPad
# User-Agent: ______________________________________________

"""

# 아이패드 유저 에이전트 값을 불러온다 (웹에서 검색하면 나옴)
IPAD_USER_AGENT = "Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10"


response = requests.get(
    "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC",
    headers={"User-Agent": IPAD_USER_AGENT,})


# 정상작동 테스트
"파이썬" in response.text


bs = BeautifulSoup(response.text, "html.parser")

# ul의 addParemt class안 li의 api_bx id를 select 한다
post_elements = bs.select("ul#addParemt li.api_bx")



# 하나만 우선 출력 테스트
post_element = post_elements[0]
post_element.select_one("div.total_tit").text  # text 만 가져옴


# 리스트로 출력
[
    post_element.select_one("div.total_tit").text
    for post_element
    in post_elements
]



# str 으로 출력
data = "\n".join([
        post_element.select_one("div.total_tit").text
        for post_element
        in post_elements
    ])


"""
# 페이지 네이션

# 1 ~ 10 페이지까지의 결과를
# CSV 파일로 저장한다.
# 함수 ( input: 키워드, 페이지수 ) => 입력받은 키워드, 입력받은 페이지수  return
# 딕셔너리의 리스트
# [{"title": "___________________________", "url": __________________, "blog_title": "________________________"}, ]
# 1-10 페이지
# 100개의 Dict => CSV 파일 형태

"""


response = requests.get("http://search.daum.net/search?w=blog&nil_search=btn&DA=NTB&enc=utf8&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
bs = BeautifulSoup(response.text, "html.parser")

# 하나만 우선 추출
post_element = post_elements[0]


# [{title:a, url:b, blog_title, c}, {           }] 형식으로 데이터 정렬


response = requests.get("http://search.daum.net/search?w=blog&nil_search=btn&DA=NTB&enc=utf8&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
bs = BeautifulSoup(response.text, "html.parser")


# 한 페이지 크롤링
[
    {
        "title": post_element.select_one("div.wrap_tit a").text,
        "url": post_element.select_one("div.wrap_tit a").attrs.get("href"),
        "blog_title": post_element.select(".info a")[1].text,
    }
    for post_element
    in bs.select("ul#blogResultUl li")
]



# 여러 페이지 크롤링

BASE_URL = "http://search.daum.net/search?w=blog&nil_search=btn&DA=PGD&enc=utf8&q={query}&page={page}&m=board"
QUERY = "파이썬"


result = [
    [
        {
            "title": post_element.select_one("div.wrap_tit a").text,
            "url": post_element.select_one("div.wrap_tit a").attrs.get("href"),
            "blog_title": post_element.select(".info a")[1].text,
        }
        for post_element
        in BeautifulSoup(
            requests.get("http://search.daum.net/search?w=blog&nil_search=btn&DA=NTB&enc=utf8&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
                        ).text, "html.parser").select("ul#blogResultUl li")
    ]
    for page
    in range(1, 3+1)
]


len(result)


# 리스트 하나에 모두 담기

posts = []

for i in range(len(result)):
    posts += result[i]


len(posts)


""" pandas 활용 """


from pandas import DataFrame

# 표로 추출
DataFrame(posts)
