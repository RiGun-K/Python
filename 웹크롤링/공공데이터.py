# 코로나 확진자 API 공공데이터 활용
from textwrap import indent
import requests
import pprint
import json
import pandas as pd
from pandas.io.json import json_normalize
from os import name
import xml.etree.ElementTree as et
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
params ={'serviceKey' : '', 'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : '20200310', 'endCreateDt' : '20200410' }

response = requests.get(url, params=params)

content = response.text     # xml 형식
p = pprint.PrettyPrinter(indent=4)  # PrttyPrinter를 통해 데이터 정렬
print(p.pprint(content))

#bs4 사용하여 xml 내 <item> 태그 분리

xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
rows = xml_obj.findAll('item')
print(rows)
"""
# 컬럼 값 조회용
columns = rows[0].find_all()
print(columns)
"""

# 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
row_list = [] # 행값
name_list = [] # 열이름값
value_list = [] #데이터값

# xml 안의 데이터 수집
for i in range(0, len(rows)):
    columns = rows[i].find_all()
    #첫째 행 데이터 수집
    for j in range(0,len(columns)):
        if i ==0:
            # 컬럼 이름 값 저장
            name_list.append(columns[j].name)
        # 컬럼의 각 데이터 값 저장
        value_list.append(columns[j].text)
    # 각 행의 value값 전체 저장
    row_list.append(value_list)
    # 데이터 리스트 값 초기화
    value_list=[]

#xml값 DataFrame으로 만들기
corona_df = pd.DataFrame(row_list, columns=name_list)
print(corona_df.head(19)) 

#DataFrame CSV 파일로 저장
corona_df.to_csv('C:/Users/RiGun/Python/Corona_kr.csv', encoding='utf-8')
