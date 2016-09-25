
# coding: utf-8

# 동적인 사이트 crawling


import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.zigbang.com/search/map?lat=37.48192596435547&lng=127.05744171142578&zoom=5")


bs = BeautifulSoup(response.text, "html.parser")

eoom_elements = bs.select(".list-item")


# 동적인 사이트라 못긁어옴
len(room_elements)
# 0

"""
# 웹 클라이언트: HTML, CSS, Javascript
#             ---------------------- 텍스트 형태
# 웹 브라우저 -> HTML 텍스트를 읽어서, Javascript 실행! => 매물 정보

# 동적인 사이트
# == ajax ( Async Javascript and XML )
# == api
# == client rendering
# == javascript


# zigbang API 찾기 (크롬 개발자 도구)

# JSON API
# JavaScript Object Notation => 자바스크립트 객체 표현법
# Javascript Object ( key => value ) == Python Dict

"""


import json


student = {
    "name": "Suchan An",
    "email": "dobestan@gmail.com",
    "skills": ["python", "javascript"]
}


# input:dict => output:string(=json)
json.dumps(student)
# '{"name": "Suchan An", "skills": ["python", "javascript"], "email": "dobestan@gmail.com"}'


# input:string(=json) => output:dict
json.loads(student_json_text)
# {'email': 'dobestan@gmail.com',
#  'name': 'Suchan An',
#  'skills': ['python', 'javascript']}


response = requests.get("https://api.zigbang.com/v1/items?detail=true&item_ids=5881377&item_ids=5910506&item_ids=5896890&item_ids=5963161&item_ids=5901022&item_ids=5872553&item_ids=5942723&item_ids=5989297&item_ids=5910011&item_ids=5954983&item_ids=5944827&item_ids=5980687&item_ids=5674847&item_ids=5994877&item_ids=5962548&item_ids=5506671&item_ids=5912354&item_ids=5979948&item_ids=5882040&item_ids=5958508&item_ids=5960660&item_ids=5964051&item_ids=5921360&item_ids=5732212&item_ids=5969169&item_ids=5789405&item_ids=5863838&item_ids=5957741&item_ids=5857887&item_ids=5964834&item_ids=5809261&item_ids=5973948&item_ids=5887819&item_ids=5964145&item_ids=5762269&item_ids=5815532&item_ids=5952275&item_ids=5897177&item_ids=5912689&item_ids=5961175&item_ids=6006296&item_ids=5923500&item_ids=5801370&item_ids=5948323&item_ids=5522144&item_ids=5954189&item_ids=5671564&item_ids=5924191&item_ids=6003127&item_ids=5809153&item_ids=6003717&item_ids=5735693&item_ids=5776190&item_ids=5987559&item_ids=5855903&item_ids=5849535&item_ids=5766193&item_ids=5992437&item_ids=5956383&item_ids=5971183")


import json


zigbang = json.loads(response.text)


# 자료구조 확인
zigbang["items"][1]["item"]["deposit"]
zigbang["items"][1]["item"]["rent"]
zigbang["items"][1]["item"]["id"]

# 개선
items = zigbang.get("items")
item = items[0]
item.get("item").get("deposit")
item.get("item").get("rent")
item.get("item").get("id")


# 필요한 정보만 딕셔너리 리스트로 추출
rooms = [
    {
        "room_id": item.get("item").get("id"),
        "room_deposit": item.get("item").get("deposit"),
        "room_rent": item.get("item").get("rent"),
    }
    for item
    in zigbang.get("items")
]


"""
# CSV 파일로 변경 ( zigbang_room.csv )

# room_id,deposit,rent
# 5985974,37000,0
# 5793633,18000,50

"""


with open("zigbang_room.csv", "w") as fp:
    fp.write("room_it,room_deposti,room_rent\n")
    fp.write("\n".join([
                "{room_id},{room_deposit},{room_rent}".format(
                    room_id=room.get("room_id"),
                    room_deposit=room.get("room_deposit"),
                    room_rent=room.get("room_rent"),
                    )
                    for room
                    in rooms
    ]))



""" # 방 모든 데이터를 json 파일로 저장 """

import json

response = requests.get("https://api.zigbang.com/v1/items?detail=true&item_ids=5881377&item_ids=5910506&item_ids=5896890&item_ids=5963161&item_ids=5901022&item_ids=5872553&item_ids=5942723&item_ids=5989297&item_ids=5910011&item_ids=5954983&item_ids=5944827&item_ids=5980687&item_ids=5674847&item_ids=5994877&item_ids=5962548&item_ids=5506671&item_ids=5912354&item_ids=5979948&item_ids=5882040&item_ids=5958508&item_ids=5960660&item_ids=5964051&item_ids=5921360&item_ids=5732212&item_ids=5969169&item_ids=5789405&item_ids=5863838&item_ids=5957741&item_ids=5857887&item_ids=5964834&item_ids=5809261&item_ids=5973948&item_ids=5887819&item_ids=5964145&item_ids=5762269&item_ids=5815532&item_ids=5952275&item_ids=5897177&item_ids=5912689&item_ids=5961175&item_ids=6006296&item_ids=5923500&item_ids=5801370&item_ids=5948323&item_ids=5522144&item_ids=5954189&item_ids=5671564&item_ids=5924191&item_ids=6003127&item_ids=5809153&item_ids=6003717&item_ids=5735693&item_ids=5776190&item_ids=5987559&item_ids=5855903&item_ids=5849535&item_ids=5766193&item_ids=5992437&item_ids=5956383&item_ids=5971183")

zigbang = json.loads(response.text)

zigbang_json = json.dumps(
    zigbang,
    open("zigbang_room.json", "w")
)




"""  마치며..

서버 => pandas, matplotlib, => 이미지 => 클라이언트
리소스 ++++
히스토그램 :: API ( JSON API )
클라이언트 자바스크립트 :: 시각화

시각화 :: d3.js, highcharts.   # 동적인 자바스크립트 라이브러리
시각화 :: 파이썬 => 이미지
         파이썬 => HTML, CSS, Javascript
                  DataFrame + Bokeh

100 시간

기본적인 연습 +++
Class ( 객체 지향 프로그래밍 ) :: People, Animal, Request, Response
                             학원:: 패스트캠퍼스, 스쿨, 웹프스,
--------------------------------------------------------------
기능 => 코드 => 완성
--------------------------------------------------------------
테스트 => 코드 => 완성 ( 테스트 주도 개발 ) :: TDD
        테스트 주도 개발...!
파이썬 테스트 코드?
--------------------------------------------------------------
pytest, unittest :: cli

Full Stack Framework, Micro Framework

dobestan@gmail.com, 01022205736


"""
