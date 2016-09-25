# coding: utf-8

"""
# Serialize, Deserialize

# JSON :: 객체 <=> 자바스크립트 객체
# Pickle :: 객체 <=> 바이너리 ( 클래스의 객체 : 0101010 ... )
# API 개발 :: Database => Django Models => ... ( Serializer ) ... => JSON API

"""

import requests

response = requests.get("https://api.zigbang.com/v1/items?detail=true&item_ids=5881377&item_ids=5910506&item_ids=5896890&item_ids=5963161&item_ids=5901022&item_ids=5872553&item_ids=5942723&item_ids=5989297&item_ids=5910011&item_ids=5954983&item_ids=5944827&item_ids=5980687&item_ids=5674847&item_ids=5994877&item_ids=5962548&item_ids=5506671&item_ids=5912354&item_ids=5979948&item_ids=5882040&item_ids=5958508&item_ids=5960660&item_ids=5964051&item_ids=5921360&item_ids=5732212&item_ids=5969169&item_ids=5789405&item_ids=5863838&item_ids=5957741&item_ids=5857887&item_ids=5964834&item_ids=5809261&item_ids=5973948&item_ids=5887819&item_ids=5964145&item_ids=5762269&item_ids=5815532&item_ids=5952275&item_ids=5897177&item_ids=5912689&item_ids=5961175&item_ids=6006296&item_ids=5923500&item_ids=5801370&item_ids=5948323&item_ids=5522144&item_ids=5954189&item_ids=5671564&item_ids=5924191&item_ids=6003127&item_ids=5809153&item_ids=6003717&item_ids=5735693&item_ids=5776190&item_ids=5987559&item_ids=5855903&item_ids=5849535&item_ids=5766193&item_ids=5992437&item_ids=5956383&item_ids=5971183")


import json

zigbang = json.loads(response.text)


# 데이터 구조 확인
zigbang.get("items")[0].get("item")

# 딕셔너리로 정리
rooms = [
    {
        "room_id": item.get("item").get("id"),
        "deposit": item.get("item").get("deposit"),
        "rent": item.get("item").get("rent"),
    }
    for item
    in zigbang.get("items")
]




""" rent average """

rent_sum = 0

for room in rooms:
    rent_sum += room["rent"]

rent_sum/len(rooms)





""" pandas DataFrame 활용 """

import pandas as pd

df = pd.DataFrame(rooms)    # rooms 는 딕셔너리의 리스트임

df.rent.mean()    # rent 평균값 계산

df.to_csv("pd_zigbang2.csv", index=False)    # csv 파일로 저장

df2 = pd.read_csv("pd_zigbang2.csv")    # csv 파일 읽기

df2.head(3)    # 위에서 3개 값만 테이블로 출력

# count, mean, std, min, 25%, 50%, 75%, max 값을 요소별로 테이블 추출
df2.describe()


# 데이터 구조 다시 확인
zigbang.get("items")[0].get("item")


# 데이터 테이블 뽑기
df3 = pd.DataFrame(
    [
        item.get("item")
        for item
        in zigbang.get("items")
    ]
)





""" filter """

df3.deposit    # deposit 요소 데이터만 추출

df3.loc[0]    # row 항목 확인하기

df3.deposit > 20000    # deposit > 20000 이상만 확인 (bool 값으로 나옴)

# bool 값을 key로 불러내면 필터한 테이블을 볼 수 있다.
df[df.deposit > 2000][df.rent > 30]





"""
# 1. Numpy         :: Numerical Python - ndarray ( vector, matrix )
# 2. Pandas        :: Row,Column Series => Row * Column => DataFrame
# 3. Matplotlib    :: Plot, Figure

"""


# You can use matplotlib inside your IPython Notebook
# by calling %matplotlib inline
# %matplotlib inline activates the inline backend
# and calls images as static pngs.


%matplotlib inline

# df 의 deposit 히스토그램
df.deposit.hist()





""" 두 사이트 데이터 비교하기 """

site_a_url = "https://api.zigbang.com/v1/items?detail=true&item_ids=5902562&item_ids=5961897&item_ids=5956585&item_ids=5599736&item_ids=5815514&item_ids=5967326&item_ids=5833868&item_ids=5959887&item_ids=5973622&item_ids=5972317&item_ids=5784089&item_ids=5824508&item_ids=5910451&item_ids=5946724&item_ids=5816541&item_ids=5956933&item_ids=5929241&item_ids=5959777&item_ids=5762426&item_ids=5988631&item_ids=5604812&item_ids=5819095&item_ids=5754867&item_ids=5861556&item_ids=5942530&item_ids=5993614&item_ids=5966156&item_ids=5984413&item_ids=5764034&item_ids=5925755&item_ids=5988322&item_ids=5901487&item_ids=5829589&item_ids=5985252&item_ids=5929533&item_ids=5823808&item_ids=5848692&item_ids=5733775&item_ids=5899785&item_ids=5828499&item_ids=5963277&item_ids=5807143&item_ids=5988621&item_ids=5937033&item_ids=5589541&item_ids=5820392&item_ids=5777686&item_ids=5810169&item_ids=5808695&item_ids=5898499&item_ids=5751720&item_ids=5884283&item_ids=5920510&item_ids=5816313&item_ids=5942307&item_ids=5861591&item_ids=5808715&item_ids=5828048&item_ids=5975775&item_ids=5687196"
site_b_url = "https://api.zigbang.com/v1/items?detail=true&item_ids=5918415&item_ids=5961139&item_ids=5903314&item_ids=5979660&item_ids=5958355&item_ids=5980168&item_ids=5938958&item_ids=5950418&item_ids=5979000&item_ids=5971565&item_ids=5922787&item_ids=5911197&item_ids=5906902&item_ids=5996079&item_ids=5780431&item_ids=5841938&item_ids=5847014&item_ids=5921321&item_ids=5992544&item_ids=5790644&item_ids=5983537&item_ids=5993783&item_ids=5979910&item_ids=5889380&item_ids=5951180&item_ids=5934321&item_ids=5965178&item_ids=5952524&item_ids=5913409&item_ids=5880897&item_ids=5981267&item_ids=5972712&item_ids=5984720&item_ids=5980482&item_ids=5762553&item_ids=5839153&item_ids=5971488&item_ids=5973881&item_ids=5959699&item_ids=5927175&item_ids=5983785&item_ids=5992662&item_ids=5993230&item_ids=5878475&item_ids=5969176&item_ids=5940259&item_ids=5971361&item_ids=5985007&item_ids=5787013&item_ids=5960205&item_ids=5784823&item_ids=5973632&item_ids=5924251&item_ids=5913995&item_ids=5979054&item_ids=5904113&item_ids=5949389&item_ids=5957093&item_ids=5906565&item_ids=5964168"


import pandas as pd
import json
import requests

# 데이터구조 확인
requests.get(site_a_url)
requests.get(site_a_url).json()
requests.get(site_a_url).json().get("items")


# site a의 테이블 출력
site_a_df = pd.DataFrame([
        item.get("item")
        for item
        in requests.get(site_a_url).json().get("items")
    ])

# site b의 테이블 출력
site_b_df = pd.DataFrame([
        item.get("item")
        for item
        in requests.get(site_b_url).json().get("items")
    ])


# [[]] 으로 키를 찾아간다 DataFrame 문법?
site_a_df = site_a_df[["id", "deposit", "rent"]]
site_b_df = site_b_df[["id", "deposit", "rent"]]

# csv로 저장
site_a_df.to_csv("site_a.csv", index=False)
site_b_df.to_csv("site_b.csv", index=False)

# csv 읽기
site_a_df = pd.read_csv("site_a.csv")
site_b_df = pd.read_csv("site_b.csv")


%matplotlib inline

# scatter
site_a_df.plot.scatter(x="deposit", y="rent", color="red")
site_b_df.plot.scatter(x="deposit", y="rent")

# histogram
site_a_df.deposit.hist(color="red")
