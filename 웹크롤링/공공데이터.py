# 코로나 확진자 API 공공데이터 활용
import requests
import pprint
import json
import pandas as pd
from pandas.io.json import json_normalize

url = 'https://api.odcloud.kr/api/15080665/v1/uddi:6377af05-8fed-484c-868b-a9a72fcb0089?page=1&perPage=10&returnType=JSON&serviceKey='

response = requests.get(url)

contents = response.text
    # print(contents)

# 문자열을 JSON 으로 변경
json_ob = json.loads(contents)
print(json_ob)
print(type(json_ob)) # JSON 타입 확인

